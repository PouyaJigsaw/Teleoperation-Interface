#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from axis_camera.msg import Axis
    # Author: Andrew Dai
    # This ROS Node converts Joystick inputs from the joy node
    # into commands for turtlesim

    # Receives joystick messages (subscribed to Joy topic)
    # then converts the joysick inputs into Twist commands
    # axis 1 aka left stick vertical controls linear speed
    # axis 0 aka left stick horizonal controls angular speed



def callback(data):
    global joystick_input

    joystick_input = data.axes[3]
       

def control_camera(joys_i):
    global next_pos_pan
    
    
    next_pos_pan -=  joys_i
    axis.pan =  int((next_pos_pan + 180) % 360) - 180    
    print(next_pos_pan,"    ", joys_i)



def start():
        
        global pub_axis
        global axis
        global joystick_input
        global next_pos_pan
        
        
        
        axis = Axis()
        joystick_input = 0

        next_pos_pan = 0 


        rospy.init_node('teleop_camera_node')

        pub_axis = rospy.Publisher('/axis/cmd', Axis, queue_size=10)

        # subscribed to joystick inputs on topic "joy"
        rospy.Subscriber("joy", Joy, callback)
        
        rate = rospy.Rate(6)


        while not rospy.is_shutdown():
            
            control_camera(joystick_input)
            pub_axis.publish(axis)
            rate.sleep()
       

        
        

        # starts the node
        
        rospy.spin()

if __name__ == '__main__':   
        start()