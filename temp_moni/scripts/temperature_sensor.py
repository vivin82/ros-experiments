#!/usr/bin/python3

import rospy
from sensor_msgs.msg import Temperature

def probe_01():
    if not hasattr(probe_01, "t"):
        probe_01.t = -10 

    result = probe_01.t
    
    if result <= 60:
        probe_01.t += 1
    else:
        probe_01.t = -10

    return result


def publisher():
    rospy.init_node("temperature_node")
    pub = rospy.Publisher('temperature_update',Temperature,queue_size=10)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        temperature_msg = Temperature()
        temperature_msg.header.seq += 1
        temperature_msg.header.stamp = rospy.Time.now()
        temperature_msg.header.frame_id = "probe_01"
        temperature_msg.temperature = probe_01()
        pub.publish(temperature_msg)
        rospy.loginfo("PRINTING TEMPERATURE ........")
        rospy.loginfo(temperature_msg)
        rate.sleep()

if __name__ == "__main__":
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass