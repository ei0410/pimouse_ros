#!/usr/bin/env python
#encoding: utf8
import rospy, sys, math
from std_msgs.msg import String

def callback(message):
    freq = int(message.data)
    rospy.loginfo("%d", freq)
    try:
        with open("/dev/buzzer0", 'w') as f:
            f.write(message.data + "\n")
    except:
        rospy.logerr("cannot write to buzzer")

rospy.init_node('buzzer_sub')
sub = rospy.Subscriber('signal', String, callback)
rospy.spin()
