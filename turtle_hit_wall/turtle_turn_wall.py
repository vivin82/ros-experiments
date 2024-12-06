import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

turtle_x=0
turtle_y=0

def wall_callback(msg):
    global turtle_x,turtle_y
    turtle_x=msg.x
    turtle_y=msg.y

def turtle_path():
    rospy.init_node('turtle_turn_wall')
    velocity_publisher=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    rospy.Subscriber('turtle1/pose',Pose,wall_callback)
    rate=rospy.Rate(6)
    vel_msg=Twist()


    while not rospy.is_shutdown():
        if turtle_x >= 9 or turtle_x <= 2 or turtle_y >=9 or turtle_y <= 1 : 
            vel_msg.linear.x=0.7
            
            vel_msg.angular.z=0.5
        else:
            vel_msg.linear.x=0.7
            
            vel_msg.angular.z=0
            
        velocity_publisher.publish(vel_msg)
        rospy.loginfo("I'm turningggggggggg")
        rate.sleep()
    
if __name__== '__main__':
    try:
        turtle_path()
    except rospy.ROSInterruptException:
        pass
    