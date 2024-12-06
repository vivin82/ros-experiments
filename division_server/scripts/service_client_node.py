
# client node
#! /usr/bin/env python


import rospy
from division_server.srv import division1,division1Response

def division_client(x,y):
    rospy.init_node('client')
    rospy.wait_for_service('division_service')
    rate = rospy.Rate(1)


    while not rospy.is_shutdown():
        try:
            divide=rospy.ServiceProxy('division_service', division1)
            response = divide(x,y)
            rospy.loginfo(response.result)
            rate.sleep()
        except rospy.ServiceException:
            rospy.logerr('division_service call failed')
            
if __name__=='__main__':
    division_client(x=78,y=67)