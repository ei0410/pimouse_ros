#!/usr/bin/env python
import sys, rospy
from pimouse_ros.msg import SwitchValues

if __name__=='__main__':
    devfile = '/dev/rtswitch0'
    rospy.init_node('switchs')
    pub = rospy.Publisher('switchs', SwitchValues, queue_size=1)

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        try:
            with open(devfile,'r') as f:
                data = f.readline().split()
                data = [ int(e) for e in data ]
                d = SwitchValues()
                d.value = data[0]
                pub.publish(d)
                print d.value
        except IOError:
            rospy.logerr("cannot read to " + devfile)

        rate.sleep()
