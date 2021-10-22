#!/usr/bin/env python
import rospy
from std_msgs.msg import Header

pub = rospy.Publisher("test", Header, queue_size=10)
rospy.init_node('test_publisher')
rate = rospy.Rate(10)
while not rospy.is_shutdown():
    header = Header()
    header.stamp = rospy.get_time()
    pub.publish(header)
    rate.sleep()
