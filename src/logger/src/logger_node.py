#!/usr/bin/env python
import rospy
import sys
from sensor_msgs.msg import JointState


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.name[1])


# In ROS, nodes are uniquely named. If two nodes with the same
# name are launched, the previous one is kicked off. The
# anonymous=True flag means that rospy will choose a unique
# name for our 'listener' node so that multiple listeners can
# run simultaneously.
rospy.init_node('edo_logger', anonymous=True)

rospy.Subscriber("joint_states", JointState, callback)

# spin() simply keeps python from exiting until this node is stopped
rospy.spin()
