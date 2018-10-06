#!/usr/bin/env python
#encoding: utf8
import unittest, rostest
import rosnode, rospy
import time
from pimouse_ros.msg import SwitchValues

class SwitchValuesTest(unittest.TestCase):
    def setUp(self):
        rospy.Subscriber('/switchs', SwitchValues, self.callback)
        self.value = SwitchValues()

    def callback(self,data):
        self.value = data
    
    def check_values(self,sw0, sw1, sw2):
        vs = self.value
        self.assertEqual(vs.value, sw0, "differenr value: sw0")
        self.assertEqual(vs.value, sw1, "differenr value: sw1")
        self.assertEqual(vs.value, sw2, "differenr value: sw2")

	def test_node_exist(self):
		nodes = rosnode.get_node_names()
		self.assertIn('/switchvalues', nodes, "node does not exist")
    
    def test_get_value(self):
        time.sleep(2)
        with open("/dev/rtswitch0","w") as f0, open("/dev/rtswitch1","w") as f1, open("/dev/rtswitch2","w") as f2:
            f0.write("0\n")
            f1.write("0\n")
            f2.write("0\n")

        time.sleep(3)

        self.check_values(0, 0, 0)

if __name__=='__main__':
    time.sleep(3)
    rospy.init_node('travis_test_switchvalues')
    rostest.rosrun('pimouse_ros', 'travis_test_switchvalues', SwitchValuesTest)
