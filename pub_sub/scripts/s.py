#!/usr/bin/python3

import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo(f"received:{msg.data}")

def listener():
    rospy.init_node("RAA24_subnode",anonymous=True)
    rospy.Subscriber("Greetings",String,callback)
    rospy.spin()

if __name__=="__main__":
    listener()