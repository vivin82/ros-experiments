import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

turtle_x=0

def wall_callback(msg):
    global turtle_x
    turtle_x=msg.x

def turtle_path():
    rospy.init_node('turtle_2')
    velocity_publisher=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    rospy.Subscriber('/turtle1/pose',Pose,wall_callback)
    rate=rospy.Rate(10)
    vel_msg=Twist()
    print("Enter direction to move the turtle:")
    
    enter_direction=input("Type 1 for right or 2 for left........\n\n")


    while not rospy.is_shutdown():
        if(enter_direction=="1"):
            
            if turtle_x < 10.0 :
                vel_msg.linear.x=1.0
                
            else:
                
                vel_msg.linear.x=0.0
                
                rospy.loginfo("Thanks I did not hit the wall")
                
            velocity_publisher.publish(vel_msg)
            
            rate.sleep()
            
        elif(enter_direction=="2"):
            
            if turtle_x > 1 :
                vel_msg.linear.x=-1.0
                
            else:
                vel_msg.linear.x=0.0
                rospy.loginfo("Thanks I did not hit the wall")
                
            velocity_publisher.publish(vel_msg)
            
            rate.sleep()
    vel_msg.linear.y=0
    vel_msg.linear.z=0
    vel_msg.angular.x=0
    vel_msg.angular.y=0
    vel_msg.angular.z=0
    
if __name__== '__main__':
    try:
        turtle_path()
    except rospy.ROSInterruptException:
        pass
    