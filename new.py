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


def callback(data):
	cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
	image = cv2.cvtColor(cv_image , cv2.COLOR_BGR2HSV)
	lower_range = np.array([30,150,50])
	upper_range = np.array([255,255,180])
	mask = cv2.inRange(image , lower_range, upper_range)
	res = cv2.bitwise_and(cv_image, cv_image, mask=mask)
	cv2.imshow("Image window", res) 


def __init__():
	bridge = CvBridge()
	image_sub = rospy.Subscriber("/camera/rgb/image_color",Image,callback)


def main():
	rospy.init_node('image_converter', anonymous=True)


if __name__ == '__main__':
	main()

