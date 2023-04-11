#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from axis_camera.msg import Axis
from event import *
from std_msgs.msg import Bool
#from view import tutorial_mode


global freeze_var
#freeze_var = True if tutorial_mode == False else freeze_var == False
freeze_var = True 

def callback(data):
    
    twist.linear.x = -2 * data.axes[1]
    twist.angular.z = 2 * data.axes[0]      

def start():
        global pub_jackal
        global twist
        
        twist =  Twist()
        


        def freeze_manager(data):
            print("event triggered: " + str(data.data) + " is received.")

            global freeze_var
            if data.data == True:
                freeze_var = True
            else:
                freeze_var = False

            


        print("number of EventManager.subscribers: " + str(len(EventManager.subscribers["unfreeze"])))
        rospy.init_node('teleop_wheel_node')

        pub_jackal = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        
        rospy.Subscriber("freeze", Bool , callback=freeze_manager)
        rospy.Subscriber("joy", Joy, callback)

        rate = rospy.Rate(30)

        while not rospy.is_shutdown():
            if freeze_var == False: pub_jackal.publish(twist)
            rate.sleep()
             

        rospy.spin()

if __name__ == '__main__':   
        start()

