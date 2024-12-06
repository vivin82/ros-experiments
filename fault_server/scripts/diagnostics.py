#!/usr/bin/python3

import rospy
from fault_server.srv import motor_status , motor_statusResponse

def diagnostics():
    rospy.init_node("diagnostics")
    m1=rospy.ServiceProxy("motor1_status",motor_status)
    m2=rospy.ServiceProxy("motor2_status",motor_status)
    m3=rospy.ServiceProxy("motor3_status",motor_status)
    
    m1_diagnose = m1()
    m2_diagnose = m2()
    m3_diagnose = m3() 
    
    rospy.loginfo(m1_diagnose)
    rospy.loginfo(m2_diagnose)
    rospy.loginfo(m3_diagnose)
    
    if m1_diagnose.response == True and m2_diagnose.response == True and m3_diagnose.response == True:
        rospy.loginfo("Joint motors check : PASS")
    else:
        rospy.logerr("JOINT MOTORS CHECK : FAIL")
        rospy.spin()
    
if __name__ =="__main__":
    diagnostics()