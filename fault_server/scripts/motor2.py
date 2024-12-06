#!/usr/bin/python3

import rospy
import random
from fault_server.srv import motor_status , motor_statusResponse

def callback(req):
    current_status=False
    message="motor 2 running" if current_status else "motor 2 not running"
    return motor_statusResponse(current_status,message)

def func():
    rospy.init_node("motor2_node")
    rospy.Service("motor2_status",motor_status,callback)
    rospy.loginfo("motor2 node is running")
    rospy.spin()
    
if __name__ =="__main__":
    func()