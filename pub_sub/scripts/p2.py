#!/usr/bin/python3

import rospy
from std_msgs.msg import String

def publisher():
    rospy.init_node("Vivin_pubnode",anonymous=True)
    pub=rospy.Publisher('Greetings',String,queue_size=20)
    rate=rospy.Rate(10)
    rospy.loginfo("")

    while not rospy.is_shutdown():
        txt="Hello, I am Vivin"
        msg=String()
        msg.data=txt
        pub.publish(msg)
        rospy.loginfo(msg.data)
        rate.sleep()    
        
if __name__=='__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass