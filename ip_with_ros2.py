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

  def __init__(self):
   #self.image_pub = rospy.Publisher("image_topic_2",Image,queue_size=10)

    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/camera/rgb/image_color",Image,self.callback)
    self.depth_sub = rospy.Subscriber("/camera/depth/image",Image,self.callback2)

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)

  

    #(rows,cols,height) = cv_.shape
    #if cols > 60 and rows > 60 :
     # cv2.circle(cv_image, (50,50), 10, 255)
    image = cv2.cvtColor(cv_image , cv2.COLOR_BGR2HSV)
    lower_range = np.array([30,150,50])
    upper_range = np.array([255,255,180])
    mask = cv2.inRange(image , lower_range, upper_range)
    res = cv2.bitwise_and(cv_image, cv_image, mask=mask)
    cv2.imshow("Image window", mask)


  def callback2(self,data):
    try:
      cv_depth = self.bridge.imgmsg_to_cv2(data, "32FC1")
    except CvBridgeError as e:
      print(e)

    cv2.imshow("Depth window", cv_depth)
    print("pixel:" , cv_depth[240][320])
    
    #print("pixel:" , mask[240][320][100])
    #cv2.waitKey(3)

    #try:
      #self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
    #except CvBridgeError as e:
      #print(e)

def main(args):
  ic = image_converter()
  rospy.init_node('image_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
