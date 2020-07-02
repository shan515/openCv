#!/usr/bin/env python
from __future__ import print_function

import roslib
roslib.load_manifest('begineer_tutorial')
import sys
import rospy
import cv2
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


def main():
  #ic = image_converter()
  rospy.init_node('image_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()




def callback(data):
    try:
      cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)

    image = cv2.cvtColor(cv_image , cv2.COLOR_BGR2HSV)
    lower_range = np.array([30,150,50])
    upper_range = np.array([255,255,180])
    mask = cv2.inRange(image , lower_range, upper_range)
    res = cv2.bitwise_and(cv_image, cv_image, mask=mask)
    cv2.imshow("Image window", res)
    #cv2.waitKey(3)
import time

def callback2(data):
	try:
	  cv_depth = bridge.imgmsg_to_cv2(data, "32FC1")
	except CvBridgeError as e:
	  print(e)

	#(rows, cols) = cv_depth.shape
	#if cols > 60 and rows > 60 :
		#cv2.circle(cv_depth, (50,50), 10, 255)
	
	cv2.imshow("Dw",cv_depth)
	# time.sleep(0.05)
	# cv2.imshow("Depth window", cv_depth)
	# print("pixel:" , cv_depth[240][320])
	print("pixel:",cv_depth[240][320])




#rospy.init_node('image_converter', anonymous=True)

bridge = CvBridge()
image_sub = rospy.Subscriber("/camera/rgb/image_mono",Image,callback)
#depth_sub = rospy.Subscriber("/camera/depth/image",Image,callback2)

#try:
 #   rospy.spin()
#except KeyboardInterrupt:
 #   print("Shutting down")


if __name__ == '__main__':
	main()


