#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist
from robot_path_controller.msg import WayPoint
from robot_path_controller.srv import Path, PathResponse
from turtlebot_goto import TurtlebotGoToEnv
from math import atan2

class TurtlebotPath(TurtlebotGoToEnv):
    def __init__(self):

        service = rospy.Service('follow_path', Path, self.handle_follow_path)

        self.robot_direction = "E"

        super(TurtlebotPath, self).__init__()
    
    def handle_follow_path(self, path):
  
        for p in range(len(path.waypoints) - 1):
            current_x = path.waypoints[p].coord[0]
            current_y = path.waypoints[p].coord[1]

            next_x = path.waypoints[p+1].coord[0]
            next_y = path.waypoints[p+1].coord[1]

            print("start: ", current_x, ",", current_y)
            print("goal: ", next_x, ",", next_y)

            dx = next_x - current_x
            dy = next_y - current_y

            if (dx > 0 and dy > 0):
                move = "NE"
            elif (dx < 0 and dy > 0):
                move = "NW"
            elif (dx < 0 and dy < 0):
                move = "SW"
            elif (dx > 0 and dy < 0):
                move = "SE"
            elif (dx == 0 and dy > 0):
                move = "N"
            elif (dx == 0 and dy < 0):
                move = "S"
            elif (dx > 0 and dy == 0):
                move = "E"
            else:
                move = "W"
            
            self.rotate(move)
            self.foward()

        return PathResponse(True)

if __name__ == '__main__':
    try:
        node = rospy.init_node('pathcontrol')
        tp = TurtlebotPath()
        rospy.spin()
    except rospy.ROSInterruptException: pass