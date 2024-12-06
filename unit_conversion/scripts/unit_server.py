#!/usr/bin/python3

import rospy
from unit_conversion.srv import unit_cnvr , unit_cnvrResponse

def calllback(msg):
    mm=msg.cm *10
    return mm

def service():
    rospy.init_node("unit_server_node")
    rospy.Service("cm_to_mm",unit_cnvr,calllback)
    rospy.loginfo("SERVICE RUNNING")
    rospy.spin()
    
if __name__== '__main__':
    service()
