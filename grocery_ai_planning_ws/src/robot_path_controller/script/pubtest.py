#!/usr/bin/env python

import rospy
from robot_path_controller.msg import WayPoint
from robot_path_controller.msg import WayPointList


rospy.init_node('tuple_node')
point = WayPoint()
point.coord = (3,2)
tuple = [point]

publisher = rospy.Publisher('/tuple', WayPointList, queue_size=1)


while not rospy.is_shutdown():
    publisher.publish(tuple)

