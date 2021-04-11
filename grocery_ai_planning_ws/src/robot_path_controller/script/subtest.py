#!/usr/bin/env python

import rospy
from robot_path_controller.msg import WayPoint
from robot_path_controller.msg import WayPointList

def callback(msg):
    path = msg.path

    print(path[0].coord[1])

rospy.init_node('subs_node')


subscriber = rospy.Subscriber('/tuple', WayPointList, callback)

rospy.spin()

