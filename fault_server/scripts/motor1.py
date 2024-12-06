#!/usr/bin/python3

import rospy
import random
from fault_server.srv import motor_status , motor_statusResponse

def callback(req):
    current_status=True
    message = "Motor 1 running" if current_status else "motor 1 not runnning"
    return motor_statusResponse(current_status,message)

def func():
    rospy.init_node("motor1_node")
    rospy.Service("motor1_status",motor_status,callback)
    rospy.loginfo("motor1 node is running")
    rospy.spin()
    
if __name__ =="__main__":
    func()