#!/usr/bin/env python


import rospy
import math
import numpy as np
from geometry_msgs.msg import Point
from geometry_msgs.msg import Vector3
from nav_msgs.msg import Odometry
from turtlebot_env import TurtlebotEnv
from robot_path_controller.msg import WayPoint

class TurtlebotGoToEnv(TurtlebotEnv):
    def __init__(self):

        super(TurtlebotGoToEnv, self).__init__()

        self.linear_forward_speed = 0.2
        # Proportional gain for angular and linear pose P control
        self.kp_w = 0.05
        self.kp_v = 1.5
        self.robot_direction = "E"

    def foward(self):
        linear_speed_vector = Vector3()
        linear_speed_vector.x = 0.0
        linear_speed_vector.y = 0.0
        linear_speed_vector.z = 0.0
        angular_speed = 0.0

        error = np.inf

        odom = self.get_odom()

        step_size = rospy.get_param("/turtlebot/step_size")

        init_x = odom.pose.pose.position.x
        init_y = odom.pose.pose.position.y
        init_yaw = self.get_yaw()
        init_pose = np.array((init_x, init_y))
        
        reference_x = init_x + step_size * math.cos(init_yaw)
        reference_y = init_y + step_size * math.sin(init_yaw)

        reference = np.array((reference_x, reference_y))

        while (abs(error) > 0.01):
            odom = self.get_odom()

            current_x = odom.pose.pose.position.x
            current_y = odom.pose.pose.position.y
            current_pose = np.array((current_x, current_y))
            init_yaw = self.get_yaw()

            error = np.linalg.norm(current_pose - reference)

            linear_speed_vector.x = self.kp_v * error

            if (np.linalg.norm(current_pose - init_pose) > step_size):
                linear_speed_vector.x = -linear_speed_vector.x
            self.move_base(linear_speed_vector, angular_speed)
            # self.rotate(self.robot_direction)

        linear_speed_vector.x = 0
        self.move_base(linear_speed_vector, angular_speed)

    def rotate(self, direction):
        linear_speed_vector = Vector3()
        linear_speed_vector.x = 0.0
        linear_speed_vector.y = 0.0
        linear_speed_vector.z = 0.0
        angular_speed = 0.0
        
        error = np.inf
        init_yaw = math.degrees(self.get_yaw())
        i_error = 0

        if (direction == "N"):
            reference = 90
            self.robot_direction = "M"
        elif (direction == "E"):
            reference = 0
            self.robot_direction = "E"
        elif (direction == "W"):
            reference = 180
            self.robot_direction = "W"
        elif (direction == "S"):
            reference = -90
            self.robot_direction = "S"
        elif (direction == "NE"):
            reference = 45
            self.robot_direction = "NE"
        elif (direction == "NW"):
            reference = 135
            self.robot_direction = "NW"
        elif (direction == "SE"):
            reference = -45
            self.robot_direction = "SE"
        else:
            reference = -135
            self.robot_direction = "SW"
        
        previous_error = reference - init_yaw
        while (abs(error) > 0.01):
            yaw = math.degrees(self.get_yaw())
            
            if (reference == 180 and yaw < 0):
                yaw += 360
            error = reference - yaw
            angular_speed = self.kp_w * error
            self.move_base(linear_speed_vector, angular_speed)
            
        angular_speed = 0
        self.move_base(linear_speed_vector, angular_speed)


