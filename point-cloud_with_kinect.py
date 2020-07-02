#!/usr/bin/env python
from __future__ import print_function
import numpy as np
import roslib
roslib.load_manifest('begineer_tutorial')
import sys
import rospy
import cv2
import math
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


__docformat__ = "restructuredtext en"

#from .registry import converts_from_numpy, converts_to_numpy


class image_converter:
    

 def __init__(self):
   
    self.image_sub = rospy.Subscriber("/camera/depth/points",Image,self.callback)

def callback(self,data):
    # global x
    
    try:
        _x = self

    
        p = _x.point_step
        pointcloud2_to_array(p, squeeze=True)
    except CvBridgeError as e:
      print(e)
    return p

def pointcloud2_to_array(cloud_msg, squeeze=True):
    ''' Converts a rospy PointCloud2 message to a numpy recordarray 
    
    Reshapes the returned array to have shape (height, width), even if the height is 1.

    The reason for using np.frombuffer rather than struct.unpack is speed... especially
    for large point clouds, this will be <much> faster.
    '''
    # construct a numpy record type equivalent to the point type of this cloud
    dtype_list = fields_to_dtype(cloud_msg.fields, cloud_msg.point_step)

    # parse the cloud into an array
    cloud_arr = np.frombuffer(cloud_msg.data, dtype_list)

    # remove the dummy fields that were added
    cloud_arr = cloud_arr[
        [fname for fname, _type in dtype_list if not (fname[:len(DUMMY_FIELD_PREFIX)] == DUMMY_FIELD_PREFIX)]]
    
    if squeeze and cloud_msg.height == 1:
        return np.reshape(cloud_arr, (cloud_msg.width,))
    else:
        return np.reshape(cloud_arr, (cloud_msg.height, cloud_msg.width))

def get_xyz_points(cloud_array, remove_nans=True, dtype=np.float):
    '''Pulls out x, y, and z columns from the cloud recordarray, and returns
	a 3xN matrix.
    '''
    # remove crap points
    if remove_nans:
        mask = np.isfinite(cloud_array['x']) & np.isfinite(cloud_array['y']) & np.isfinite(cloud_array['z'])
        cloud_array = cloud_array[mask]
    
    # pull out x, y, and z values
    points = np.zeros(cloud_array.shape + (3,), dtype=dtype)
    points[...,0] = cloud_array['x']
    points[...,1] = cloud_array['y']
    points[...,2] = cloud_array['z']

    return points


if __name__ == "__main__":
    ic = image_converter
    #pointcloud2_to_array(p, squeeze = True)
    rospy.init_node('image_converter', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")


    
 #   global x
    # pointcloud2_to_array(p, squeeze=True)
    #get_xyz_points(cloud_array, remove_nans=True, dtype=np.float)
    
