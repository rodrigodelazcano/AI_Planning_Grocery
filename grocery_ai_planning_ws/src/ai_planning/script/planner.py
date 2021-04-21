#!/usr/bin/env python3

import pyhop2
from a_star import astar
from map import Map
from robot_path_controller.srv import Path, PathResponse
from robot_path_controller.msg import WayPoint
import rospy
from gazebo_msgs.srv import GetModelState
from check_result import check_result, pause, set_trace

#########################################################
## Grocery Plan #########################################

domain_name = 'groceryplan'

# Create a new domain to contain the methods and operators
pyhop2.Domain(domain_name)


# states and rigid relations

rigid = pyhop2.State('rigid relations')
# These types are used by the 'is_a' helper function, later in this file
rigid.types = {
    'person':   ['robot'],
    'location': ['coliflower', 'chicken']}

# prototypical initial state
state0 = pyhop2.State('state0')
state0.loc = {'robot':(1,1), 'coliflower': (1.54, 5.4), 'chicken': (2.06, 10.73)}
# state0.wayp = []


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

pyhop2.declare_actions(move_robot)


# Commands:

def c_move_robot(state,r,y):
    if is_a(r,'person') and is_a(y,'location') and state.loc[r] != state.loc[y]:
        
        resp_location = robot_location('mobile_base', 'world')
        coord = (resp_location.pose.position.x, resp_location.pose.position.y)

        wayp = astar(coord, state.loc[y], 0.4)

        path = wayp
        path_msg = []

        for point in path:
            waypoint = WayPoint()
            waypoint.coord = point
            path_msg.append(waypoint)
        
        resp = follow_path(path_msg)
        # print(resp)

        state.loc[r] = state.loc[y]
        return state

pyhop2.declare_commands(c_move_robot)


# Methods:

def shop(state,r,y):
    if is_a(r,'person') and is_a(y,'location'):
        if state.loc[r] != state.loc[y]:
            return [('move_robot',r,y)]

def do_nothing(state,r,y):
	if is_a(r,'person') and is_a(y,'location'):
		if state.loc[r] == state.loc[y]:
			return []


pyhop2.declare_task_methods('groceryshop', do_nothing, shop)

# Running the examples

print('-----------------------------------------------------------------------')
print(f"Created the domain '{domain_name}'.")


##### GROCERY PLAN ENDS #################################
#########################################################

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


        state1 = state0.copy()
        state1.display(heading='\nInitial state is')

        pause()
        print("Use find plan to plan how to get Robot from start to the item.")

        expected = [('move_robot', 'robot', 'coliflower')]

        result = pyhop2.find_plan(state1, [('groceryshop','robot','coliflower')],verbose=3)
        check_result(result, expected)

        pause()
        new_state = pyhop2.run_lazy_lookahead(state1,[('groceryshop','robot','coliflower')],verbose=3)
        pause()

        # total_path = state0.wayp
        
        # item_ctr = 0

        # while(total_path):

        # 	path = total_path.pop(0)

	       #  path_msg = []
	       #  for point in path:
	       #      waypoint = WayPoint()
	       #      waypoint.coord = point
	       #      path_msg.append(waypoint)
	        
	       #  resp = follow_path(path_msg)

	       #  item_ctr += 1
	       #  print('Item No: ', item_ctr, 'picked!!')

        # print(resp)
        
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)