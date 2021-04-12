#!/usr/bin/env python3

import pyhop2
from a_star import astar
from map import Map
from robot_path_controller.srv import Path, PathResponse
from robot_path_controller.msg import WayPoint
import rospy

if __name__ == '__main__':
    node = rospy.init_node('a_star_planner')
    rospy.wait_for_service('follow_path')
    step_size = 0.4
    start = (1.9, 5.59)
    goal =(1.9, 7)

    try:
        rospy.set_param("turtlebot/step_size", step_size)
        follow_path = rospy.ServiceProxy('follow_path', Path)
        path = astar(start, goal, step_size)
        print(path)
        path_msg = []
        for point in path:
            waypoint = WayPoint()
            waypoint.coord = point
            path_msg.append(waypoint)
        
        resp = follow_path(path_msg)

        print(resp)
        
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)