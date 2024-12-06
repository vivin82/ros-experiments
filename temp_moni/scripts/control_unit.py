#! usr/bin/python3

import rospy
from sensor_msgs.msg import Temperature
    
def call_back(msg):
    rospy.loginfo(msg)


def subscriber():
    rospy.init_node("control_unit_01")
    rospy.Subscriber('temperature_update',Temperature,callback=call_back)
    rospy.loginfo("RECEIVING TEMPERATURE READINGS")
    rospy.spin()
        
    
if __name__ == "__main__":
    subscriber()