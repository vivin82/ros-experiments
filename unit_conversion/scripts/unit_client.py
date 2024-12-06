#!/usr/bin/python3

import rospy
import random
from unit_conversion.srv import unit_cnvr

def client():
    rospy.init_node("unit_client_node")
    unit_cnr = rospy.ServiceProxy("cm_to_mm", unit_cnvr)
    rate=rospy.Rate(1)
    while not rospy.is_shutdown():
        rospy.loginfo("reading sensor data[distance]............")
        dist_in_cm= random.random() *100
        rospy.loginfo(f"distance : {dist_in_cm} cm")
        rospy.loginfo("requesting unit conversion service....")
        dist_in_mm=unit_cnr(dist_in_cm).mm
        rospy.loginfo(f"distance in mm : {dist_in_mm} mm\n\n\n")
        rate.sleep()
        
if __name__== "__main__":
    client()
