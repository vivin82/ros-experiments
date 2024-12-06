import rospy
from geometry_msgs.msg import Twist

def hit():
    rospy.init_node('turtle1')
    pub=rospy.Publisher('turtle1/cmd_vel',Twist,queue_size=10)
    rate=rospy.Rate(10)

    msg=Twist()
    msg.linear.x=1

    while not rospy.is_shutdown():
        rospy.loginfo("I hit the walllllll")
        pub.publish(msg)
        rate.sleep()
    
if __name__== '__main__':
    hit()
    