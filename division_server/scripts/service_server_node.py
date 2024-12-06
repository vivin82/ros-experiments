# server node
#! /usr/bin/env python

# from __future__ import print_function
import rospy
from division_server.srv import division1, division1Response 
import rospy

def callback_fn(request):
    return division1Response (request.a / request.b)

def division():
    rospy.init_node('division_server_node')
    service=rospy.Service('division_service',division1,callback_fn)
    print('ready to divide')
    rospy.spin()

if __name__=='__main__':
    division()