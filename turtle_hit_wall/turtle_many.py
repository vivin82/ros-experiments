#!/usr/bin/env python

import rospy
from turtlesim.srv import Spawn


def add_turtles():
        rospy.init_node('turtle_spawn')
        rospy.wait_for_service('/spawn')
        spawn_turtle = rospy.ServiceProxy('/spawn', Spawn)
        
        
        spawn_turtle(3.5, 2.0, 2.0, 'Bravo')  
        spawn_turtle(5.5, 2.0, 2.0, 'Charlie')  
        spawn_turtle(7.5, 2.0, 2.0, 'Delta')  

if __name__ == "__main__":
        add_turtles()
