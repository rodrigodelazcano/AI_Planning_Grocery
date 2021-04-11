#!/usr/bin/env python


import rospy
import math
from geometry_msgs.msg import Point
from geometry_msgs.msg import Vector3
from nav_msgs.msg import Odometry
from turtlebot_env import TurtlebotEnv
from robot_path_controller.msg import WayPoint, WayPointList

class TurtlebotGoToEnv(TurtlebotEnv):
    def __init__(self):

        # Here we will add any init functions prior to starting the MyRobotEnv
        super(TurtlebotGoToEnv, self).__init__()

        self.linear_forward_speed = 0.25
        self.angular_speed = 0.25
    
    def _set_action(self, action):
        linear_speed_vector = Vector3()
        linear_speed_vector.x = 0.0
        linear_speed_vector.y = 0.0
        linear_speed_vector.z = 0.0
        angular_speed = 0.0

        self.reset_odometry()

        init_state = self.get_odom()
        init_yaw = self.get_yaw()
        print(init_yaw)
        if init_yaw < 0:
            init_yaw = init_yaw + math.pi * 2

        print(init_yaw)
        rate = rospy.Rate(10) # 10hz

        # We convert the actions to speed movements to send to the parent class of Parrot
        if action == 0: #FORWARD
            
            linear_speed_vector.x = self.linear_forward_speed
            self.last_action = "FORWARD"
            while not rospy.is_shutdown():
                self.move_base(linear_speed_vector, angular_speed)
                current_state = self.get_odom()
                
                d = math.sqrt(pow((current_state.pose.pose.position.x - init_state.pose.pose.position.x),2) + pow((current_state.pose.pose.position.y - init_state.pose.pose.position.y),2))
                
                if d>=0.25:
                    linear_speed_vector.x = 0.0
                    self.move_base(linear_speed_vector, angular_speed)
                    break

        elif action == 1: #LEFT
            # angular_speed = self.angular_speed
            self.last_action = "TURN_LEFT"
            begin_time = rospy.get_time()
            duration = rospy.Time(25).to_sec()
            end_time = duration + begin_time
            target_rad = init_yaw + 45 * math.pi/180
            while (end_time > rospy.get_time()):
                odom = self.get_odom()
                yaw = self.get_yaw()
                if yaw < 0:
                    yaw = yaw + math.pi * 2
                angular_speed = 0.6 * (target_rad-yaw)
                self.move_base(linear_speed_vector,
		                       angular_speed)
                rate.sleep()
	            

        elif action == 2: #RIGHT
            # angular_speed = self.angular_speed
            self.last_action = "TURN_RIGHT"
            begin_time = rospy.get_time()
            duration = rospy.Time(25).to_sec()
            end_time = duration + begin_time
            target_rad = init_yaw - 45 * math.pi/180
            while (end_time > rospy.get_time()):
                odom = self.get_odom()
                yaw = self.get_yaw()
                if yaw < 0:
                    yaw = yaw + math.pi * 2
                angular_speed = 0.6 * (target_rad-yaw)
                self.move_base(linear_speed_vector,
		                       angular_speed)
                rate.sleep()	
