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

class image_converter:

  def __init__(self ):
   
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/camera/rgb/image_color",Image,self.callback)
    self.depth_sub = rospy.Subscriber("/camera/depth/image",Image,self.callback2)


  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)

    image = cv2.cvtColor(cv_image , cv2.COLOR_BGR2HSV)
    lower_range = np.array([30,150,50])
    upper_range = np.array([255,255,180])
    mask = cv2.inRange(image , lower_range, upper_range)
    res = cv2.bitwise_and(cv_image, cv_image, mask=mask)
    cv2.imshow("Image window", cv_image)
    print(cv_image)
    cv2.waitKey(5)
class image_depth:

  def __init__(self):
   
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/camera/rgb/image_color",Image,self.callback)
    self.depth_sub = rospy.Subscriber("/camera/depth/image",Image,self.callback2)


  def callback2(self,data):
    try:
      cv_depth = self.bridge.imgmsg_to_cv2(data, "32FC1")
    except CvBridgeError as e:
      print(e)


    (rows, columns) = cv_depth
    cv2.imshow("Depth window", cv_depth)
    print("pixel:" , cv_depth[240][320])
    print(cv_depth)
    cv2.waitKey(5)


def main(args):
  ic = image_converter()
  d = image_depth()
  rospy.init_node('image_converter', anonymous=True)
  #rospy.init_node('image_depth', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)

