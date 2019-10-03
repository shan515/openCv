import sensor_msgs.point_cloud2 as pc2
def on_scan(self, scan):
    rospy.loginfo("Got scan, projecting")
    cloud = self.laser_projector.projectLaser(scan)
    gen = pc2.read_points(cloud, skip_nans=True, field_names=("x", "y", "z"))
    self.xyz_generator = gen
fmt = _get_struct_fmt(cloud.is_bigendian, cloud.fields, field_names)
width, height, point_step, row_step, data, isnan = cloud.width, cloud.height, cloud.point_step, cloud.row_step, cloud.data, math.isnan
unpack_from = struct.Struct(fmt).unpack_from