#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import UInt16

rospy.init_node('buzzer_pub')
pub = rospy.Publisher('signal', UInt16, queue_size=10)
rate = rospy.Rate(10)
while not rospy.is_shutdown():
    number = UInt16()
    direction = raw_input('If you want listen buzzer, push [f] button.')
    if 'f' in direction:
        number.data = 400
        pub.publish(number)
    else:
        number.data = 0
        pub.publish(number)
    rate.sleep()
