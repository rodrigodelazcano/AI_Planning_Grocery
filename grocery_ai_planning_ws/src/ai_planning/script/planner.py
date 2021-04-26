#!/usr/bin/env python3

import pyhop2
from a_star import astar
from gbfs import gbfs
from map import Map
from renderer import Renderer
from robot_path_controller.srv import Path, PathResponse
from robot_path_controller.msg import WayPoint
import rospy
from gazebo_msgs.srv import GetModelState
from check_result import check_result, pause, set_trace
from products import Products
import numpy as np

prod = Products()
prod.seed(1)
item_list = prod.get_random_list()
item_list.append('cashier')
renderer = Renderer()

#########################################################
## Grocery Plan #########################################
# loc = {'robot': (7.4, 12.85), 'brocoli': (1.54, 5.4), 'cucumber': (1.54, 7.91), 'salt': (8.39, 4.79), 'watermelon': (5.1, 8.44), 'strawberry': (2.31, 6.36), 'potato': (3.58, 7.44), 'hamburger': (7.4, 12.85)}

domain_name = 'groceryplan'


# Create a new domain to contain the methods and operators
pyhop2.Domain(domain_name)


# states and rigid relations

rigid = pyhop2.State('rigid relations')
# These types are used by the 'is_a' helper function, later in this file
rigid.types = {
    'person':   ['robot'],
    'location': item_list}

# prototypical initial state
state0 = pyhop2.State('state0')
state0.loc = {'robot':(1,1)}
state0.cost = {'robot': 0}

# adding items in the list
for item in item_list:
	state0.loc[item] = prod.product_list[item]


# Helper functions:

def is_a(variable,type):
    """
    In most classical planners, one would declare data-types for the parameters
    of each action, and the data-type checks would be done by the planner.
    Pyhop 2 doesn't have a way to do that, so the 'is_a' function gives us a
    way to do it in the preconditions of each action, command, and method.
    
    'is_a' doesn't implement subtypes (e.g., if rigid.type[x] = y and
    rigid.type[x] = z, it doesn't infer that rigid.type[x] = z. It wouldn't be
    hard to implement this, but it isn't needed in the simple-travel domain.
    """
    return variable in rigid.types[type]


# Actions:

def move_robot(state,r,y):
    if is_a(r,'person') and is_a(y,'location') and state.loc[r] != state.loc[y]:
        
        # global state0
        
        # state.wayp.append(astar(state.loc[r],state.loc[y], 0.4))
        state.loc[r] = state.loc[y]
        # state0 = state
        return state

def pick_item(state, r, y):
	if is_a(r,'person') and is_a(y,'location') and state.loc[r] == state.loc[y]:
		state.loc[y] = state.loc[r]
		print(y, ' picked !!')
		return state

def pay_robot(state, r, y):
	if is_a(r,'person') and is_a(y,'location') and state.loc[r] == state.loc[y]:
		state.cost[r] = 0
		print(r, ' paid !!')
		return state


pyhop2.declare_actions(move_robot, pick_item, pay_robot)


# Commands:

def c_move_robot(state,r,y):
    if is_a(r,'person') and is_a(y,'location') and state.loc[r] != state.loc[y]:
        
        resp_location = robot_location('mobile_base', 'world')
        coord = (resp_location.pose.position.x, resp_location.pose.position.y)
        
        #######################################
        ### PLANNING WITHOUT FINITE HORIZON ###
        #######################################
        # wayp = astar(coord, state.loc[y], 0.4)
        # path = wayp
        # renderer.draw_Astar_path(path)
        # path_msg = []
        # state.cost[r] = len(path) * 0.4
        # for point in path:
        #     waypoint = WayPoint()
        #     waypoint.coord = point
        #     path_msg.append(waypoint)
        
        # resp = follow_path(path_msg)

        # resp_location = robot_location('mobile_base', 'world')
        # coord = (resp_location.pose.position.x, resp_location.pose.position.y)

        ####################################
        ### PLANNING WITH FINITE HORIZON ###
        ####################################
        distance_goal = np.linalg.norm(np.array(coord) - np.array(state.loc[y]))
        while(distance_goal > 0.5):
            
            wayp = astar(coord, state.loc[y], 0.4)

            path = wayp
            path_msg = []

            if len(path) >= 4:
                state.cost[r] += 4 * 0.4
                renderer.draw_Astar_path(path[:3])
                for point in path[:3]:
                    waypoint = WayPoint()
                    waypoint.coord = point
                    path_msg.append(waypoint)
            else:
                state.cost[r] += len(path) * 0.4
                renderer.draw_Astar_path(path)
                for point in path:
                    waypoint = WayPoint()
                    waypoint.coord = point
                    path_msg.append(waypoint)

            resp = follow_path(path_msg)

            resp_location = robot_location('mobile_base', 'world')
            coord = (resp_location.pose.position.x, resp_location.pose.position.y)

            distance_goal = np.linalg.norm(np.array(coord) - np.array(state.loc[y]))
        
        # Final state location of the robot
        state.loc[r] = state.loc[y]

        return state

def c_pick_item(state, r, y):
	if is_a(r,'person') and is_a(y,'location') and state.loc[r] == state.loc[y]:
		state.loc[y] = state.loc[r]
		print(y, ' picked !!')
		return state

def c_pay_robot(state, r, y):
	if is_a(r,'person') and is_a(y,'location') and state.loc[r] == state.loc[y]:
		state.cost[r] = 0
		print(r, ' paid !!')
		return state

pyhop2.declare_commands(c_move_robot, c_pick_item, c_pay_robot)


# Methods:

def shop(state,r,y):
    if is_a(r,'person') and is_a(y,'location'):
        if state.loc[r] != state.loc[y]:
            return [('move_robot',r,y), ('pick_item', r, y), ]

def do_nothing(state,r,y):
	if is_a(r,'person') and is_a(y,'location'):
		if state.loc[r] == state.loc[y]:
			return []

def pay_money(state, r, y):
	if is_a(r,'person') and is_a(y,'location'):
		if state.loc[r] == state.loc[y] and state.cost[r] != 0:
			return [('pay_robot', r, y)]

def paid(state, r, y):
	if is_a(r,'person') and is_a(y,'location'):
		if state.loc[r] == state.loc[y] and state.cost[r] == 0:
			return []



pyhop2.declare_task_methods('groceryshop', do_nothing, shop)
pyhop2.declare_task_methods('pay', paid, pay_money)


# Running the examples

print('-----------------------------------------------------------------------')
print(f"Created the domain '{domain_name}'.")

############################
##### GROCERY PLAN ENDS ####
############################
if __name__ == '__main__':

    
    pyhop2.set_current_domain(domain_name)
    pyhop2.print_domain()

    node = rospy.init_node('a_star_planner')
    rospy.wait_for_service('follow_path')
    step_size = 0.4

    try:
        rospy.set_param("turtlebot/step_size", step_size)
        follow_path = rospy.ServiceProxy('follow_path', Path)
        robot_location = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)

        # resp_location = robot_location('mobile_base', 'world')
        # coord = (resp_location.pose.position.x, resp_location.pose.position.y)
        
        #####################################################

        # Pyhop2 main()


        new_state = state0.copy()
        new_state.display(heading='\nInitial state is')

        print("Use find plan to plan how to get Robot from start to the item.")
        
        renderer.draw_product_location(item_list)     # Draw product location with distance threshold
        
        start_time = rospy.get_rostime()
        ##########################
        ### FOLLOW RANDOM LIST ###
        ##########################
        # renderer.draw_random_list(item_list)        # Draw the path sequence when the products are retrieved randomly
        # for item in item_list:        	
        # 	new_state = pyhop2.run_lazy_lookahead(new_state,[('groceryshop','robot', item)],verbose=3)
        
        ################################
        ### FOLLOW GBFS ORDERED LIST ###
        ################################
        GBFS_ordered_list = gbfs(item_list[:-1])
        GBFS_ordered_list.append('cashier')
        renderer.draw_GBFS_list(GBFS_ordered_list)    # Draw the path sequence when the proucts are retrieved after being order with GBFS algorithm
        
        for item in GBFS_ordered_list:        	
        	new_state = pyhop2.run_lazy_lookahead(new_state,[('groceryshop','robot', item)],verbose=3)
        
        final_state = pyhop2.run_lazy_lookahead(new_state,[('pay','robot', GBFS_ordered_list.pop())],verbose=3)

        end_time = rospy.get_rostime()
        renderer.draw_duration_cost(end_time.to_sec() - start_time.to_sec(), new_state.cost['robot'])
        
        renderer.render()  # render the map info

        
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)