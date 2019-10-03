#import rospy
#from std_msgs.msg import String
#from begineer_tutuorial.msg import custom_array ##custom message
#import sys

    #!/usr/bin/env python
    # license removed for brevity
import rospy
from std_msgs.msg import String
abc=String()
rospy.init_node("start")



def callback(msg):
	#print(msg.data)
	pub.publish(abc)

sub=rospy.Subscriber("/camera/depth/points",String,callback)

if __name__ == '__main__':
 try:
   callback()
 except rospy.ROSInterruptException:
   pass

