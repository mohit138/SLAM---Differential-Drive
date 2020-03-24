#!/usr/bin/env python

import rospy
import math
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from bot_l.msg import motion
rospy.init_node('base_controller')

current_time = rospy.Time.now()
prev_time= rospy.Time.now()

vx=0
vy=0
vth=0

x=0
y=0
th=0

def move(msg):
	global vx,vy,vth
	vx=msg.linear.x
	vy=msg.linear.y
	vth=msg.angular.z
	#print vx

sub = rospy.Subscriber('cmd_vel_mux/input/teleop' , Twist, move)
pub = rospy.Publisher('motion' , motion, queue_size=10)
rate = rospy.Rate(100)

mot = motion()
while not rospy.is_shutdown() :
	current_time = rospy.Time.now()
	dt=(current_time - prev_time).to_sec()
	delta_x = (vx * math.cos(th) - vy * math.sin(th)) * dt
	delta_y = (vx * math.sin(th) + vy * math.cos(th)) * dt
	delta_th = vth * dt;
	
	x=x+float(delta_x)
	y=y+float(delta_y)
	th=th+float(delta_th)
	
	#print mot
	mot.x=x
	mot.y=y
	mot.th=th
	
	pub.publish(mot)
	prev_time= rospy.Time.now()
	rate.sleep()

	
	


