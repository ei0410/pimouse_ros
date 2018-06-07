#!/usr/bin/env python
import rospy
from std_msgs.msg import String

rospy.init_node('buzzer_pub')
pub = rospy.Publisher('signal', String, queue_size=10)
rate = rospy.Rate(10)
while not rospy.is_shutdown():
    strings = String()
    direction = raw_input('f: forward > ')
    if 'f' in direction:
        strings.data = "400"
        pub.publish(strings)
    else:
        strings.data = "0"
        pub.publish(strings)
    rate.sleep()
