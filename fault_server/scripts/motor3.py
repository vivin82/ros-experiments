#!/usr/bin/python3

import rospy
import random
from fault_server.srv import motor_status , motor_statusResponse

def callback(req):
    current_status=True
    message="motor 3 is running" if current_status else "motor 3 is not running"
    return motor_statusResponse(current_status,message)

def func():
    rospy.init_node("motor3_node")
    rospy.Service("motor3_status",motor_status,callback)
    rospy.loginfo("motor3 node is running")
    rospy.spin()
    
if __name__ =="__main__":
    func()