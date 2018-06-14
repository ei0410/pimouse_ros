#!/usr/bin/env python
#encoding: utf8
import rospy, sys, math
from std_msgs.msg import String
from std_msgs.msg import UInt16

def callback(message):
    #rospy.loginfo("%d", message)
    print message
    try:
        with open("/dev/rtbuzzer0", 'w') as f:
            f.write(str(message) + "\n")
    except:
        rospy.logerr("cannot write to buzzer")

if __name__=='__main__':
    rospy.init_node('buzzer_sub')
    sub = rospy.Subscriber('signal', UInt16, callback)
    rospy.spin()
