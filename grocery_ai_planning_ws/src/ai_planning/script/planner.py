#!/usr/bin/env python3

import pyhop2
from a_star import astar
from map import Map
from robot_path_controller.srv import Path, PathResponse
from robot_path_controller.msg import WayPoint
import rospy
import groceryplan
from check_result import check_result, pause, set_trace

pyhop2.set_current_domain(groceryplan.domain_name)
pyhop2.print_domain()

if __name__ == '__main__':
    node = rospy.init_node('a_star_planner')
    rospy.wait_for_service('follow_path')
    step_size = 0.4
    start = (1.9, 5.59)
    goal =(1.9, 7)

    try:
        rospy.set_param("turtlebot/step_size", step_size)
        follow_path = rospy.ServiceProxy('follow_path', Path)
        
        #####################################################

        # Pyhop2 main()

        state1 = groceryplan.state0.copy()
        state1.display(heading='\nInitial state is')

        pause()
        print("Use find plan to plan how to get Robot from start to the item.")

        expected = [('move_robot', 'robot', 'item')]

        result = pyhop2.find_plan(state1, [('groceryshop','robot','item')],verbose=3)
        check_result(result, expected)

        # pause()
        # new_state = pyhop2.run_lazy_lookahead(state1,[('groceryshop','robot','item')],verbose=3)
        # pause()

        path = groceryplan.state0.wayp
        
        path_msg = []
        for point in path:
            waypoint = WayPoint()
            waypoint.coord = point
            path_msg.append(waypoint)
        
        resp = follow_path(path_msg)

        print(resp)
        
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)