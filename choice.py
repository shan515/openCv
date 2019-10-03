#!/usr/bin/env python
from __future__ import print_function
import numpy as np
import roslib
roslib.load_manifest('begineer_tutorial')
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

def switch():
    print ("The color of block to be picked")2
    print ("1.Red  2.Blue  3.Green  4.Orange")
    x = input (int)
    
if __name__ == '__main__':
    switch()
