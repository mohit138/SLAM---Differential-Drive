#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
rospy.init_node('topic_jumper')

def callback(msg):
	pic = Image()
	pub.publish(pic)

image_topic="/camera/depth/image"
sub = rospy.Subscriber(image_topic, Image, callback)
pub = rospy.Publisher('image', Image,queue_size=10)
rospy.spin()
