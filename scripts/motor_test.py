#!/usr/bin/env python
#encoding: utf8
import sys, rospy, math
from pimouse_ros.msg import MotorFreqs
from geometry_msgs.msg import Twist

try:
    with open("/dev/rtmotoren0", 'w') as f:
        f.write("1\n")
except:
    rospy.logerr("cannot write")

try:
    with open("/dev/rtmotor_raw_r0", 'w') as rf:
        rf.write("400\n")
except:
    rospy.logerr("cannot motor")

rospy.init_node('motor')

rospy.spin()
