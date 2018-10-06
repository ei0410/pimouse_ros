#!/usr/bin/env python
import sys, rospy
from pimouse_ros.msg import SwitchValues

if __name__=='__main__':
    devfile0 = '/dev/rtswitch0'
    devfile1 = '/dev/rtswitch1'
    devfile2 = '/dev/rtswitch2'
    rospy.init_node('switchs')
    pub = rospy.Publisher('switchs', SwitchValues, queue_size=1)

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        try:
            with open(devfile0,'r') as f0, open(devfile1,'r') as f1, open(devfile2,'r') as f2:
                data0 = f0.readline().split()
                data1 = f1.readline().split()
                data2 = f2.readline().split()
                data0 = [ int(e) for e in data0 ]
                data1 = [ int(e) for e in data1 ]
                data2 = [ int(e) for e in data2 ]
                d0 = SwitchValues()
                d1 = SwitchValues()
                d2 = SwitchValues()
                d0.value = data0[0]
                d1.value = data1[0]
                d2.value = data2[0]
                pub.publish(d0)
                pub.publish(d1)
                pub.publish(d2)
                print d0.value, d1.value, d2.value
        except IOError:
            rospy.logerr("cannot read to " + devfile0)
            rospy.logerr("cannot read to " + devfile1)
            rospy.logerr("cannot read to " + devfile2)

        rate.sleep()
