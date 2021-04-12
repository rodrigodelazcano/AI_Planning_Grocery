#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist
from std_msgs.msg import Empty
from sensor_msgs.msg import Imu
from tf.transformations import euler_from_quaternion
from robot_path_controller.msg import WayPoint

class TurtlebotEnv(object):
    def __init__(self):

        self.odom = None
        self.imu = None
        
        self._cmd_vel_pub = rospy.Publisher('/mobile_base/commands/velocity',
                                                Twist, queue_size = 1)

        rospy.Subscriber('/odom', Odometry, self._odom_callback)
        rospy.Subscriber('/mobile_base/sensors/imu_data', Imu, self._imu_callback)

        self._odom_reset = rospy.Publisher('/mobile_base/commands/reset_odometry', Empty, queue_size=1)
    
    def _odom_callback(self, msg):
        self.odom = msg
    
    def _imu_callback(self, msg):
        self.imu = msg

    def get_odom(self):
        return self.odom
    
    def get_yaw(self):

        return self.get_yaw_from_quaternion(self.imu.orientation)

    
    def move_base(self, linear_speed_vector, angular_speed):

        speed = Twist()
        speed.linear.x = linear_speed_vector.x
        speed.linear.y = linear_speed_vector.y
        speed.linear.z = linear_speed_vector.z
        speed.angular.z = angular_speed

        self._cmd_vel_pub.publish(speed)
    
    def reset_odometry(self):
        empty = Empty()
        empty = []
        self._odom_reset.publish()

    def get_yaw_from_quaternion(self, quaternion_vector):
        # We convert from quaternions to euler
        orientation_list = [quaternion_vector.x,
                            quaternion_vector.y,
                            quaternion_vector.z,
                            quaternion_vector.w]

        roll, pitch, yaw = euler_from_quaternion(orientation_list)
        return yaw
