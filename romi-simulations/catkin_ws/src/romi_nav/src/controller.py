#! /usr/bin/env python 
import rospy 
from 

rospy.init_node("speed_controller") 

// subscribe to odometry so we know the position of the robot at any time
sub = rospy.Subscriber("/odometry/filtered", Odometry, newOdom) 
