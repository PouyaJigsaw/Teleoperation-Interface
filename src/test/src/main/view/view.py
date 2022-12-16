#!/usr/bin/env python3

import rospy
import numpy as np
import cv2
from playsound import *
from state import *
from tkinter import * 
from PIL import ImageTk
from axis_camera.msg import Axis
import PIL.Image
from canvas import *
from camera import * 
from avatar import *
from dialogue import *
from button import *
from jackalAI import *
from tagdetector import *
import socket
import threading

sound_mode = True
# change this based on experiments
  
def main():
    root = Tk()
    root.geometry("1920x1080")
    root.title("Jackal Teleoperator GUI")
    
    #jackal = Avatar(root, javatar_info,javatar_images)
    cursor_canvas_small = CursorCanvas(root, small_canvas_info)
    cursor_canvas_small.disable()
    cursor_canvas_big = CursorCanvas(root, big_canvas_info)

    

    if camera_available == True:    
        rospy.init_node("viewer", anonymous= True)
        rospy.loginfo("viewer node started ...")
        currentangle = rospy.wait_for_message("/axis/state", Axis).pan # might be a problem
        #TODO: make the camera tilt
        #rospy.Subscriber("/axis/cmd", Axis, change_angle, callback_args=(cursor) queue_size=1) #TODO: Fix cursor change!
    
    
    x = threading.Thread(target=server_program)
    x.start()
    #bar_canvas, danger_canvases, task_canvas, view_back, view_front, manual_button, auto_button, dialogue_text, yes_button, no_button, timer_canvas, #start_button, score_canvas = widget_init(root)

    #view_back, view_front, dialogue_text = widget_init(root)
    view_back, view_front, dialogue_text = widget_init(root)
    subscribe("receive_command_voice", play_sounds)
    #print(cmd)
    #tag_detector = TagDetector()
    #gui_sfm = TeleopGUIMachine(timer_canvas, dialogue_text, start_button, yes_button, no_button, manual_button, auto_button, bar_canvas, danger_canvases)
    
    #start_button.add_event(gui_sfm.s01)
    #yes_button.add_event(gui_sfm.s45)
    #no_button.add_event(gui_sfm.s46)
    #task_canvas.add_fsm(gui_sfm)
    #bind(root, cursor_canvas_small, cursor_canvas_big, bar_canvas, danger_canvases, task_canvas, view_back, view_front, manual_button, auto_button)
    bind(root, cursor_canvas_small, cursor_canvas_big, view_back, view_front)
       

    
    
    if camera_available == True:
        try:
            
            root.mainloop()
        except rospy.ROSInterruptException:
            pass
    else:
            root.mainloop()


def widget_init(root):
    #bar_canvas = BarCanvas(root, bar_canvas_info_main, danger= False)
    #danger_canvases = (BarCanvas(root, bar_canvas_info1,danger= True),
                           #BarCanvas(root,bar_canvas_info2, danger= True),
                           #  BarCanvas(root,bar_canvas_info3, danger = True))
    if not sound_mode: dialogue_text = DialogueBox(root, dbox_info, mega_dict)
    else: dialogue_text = None
    #task_canvas = TaskCanvas(root, task_canvas_info)
    view_back = CameraView(root, flir_info, camera_available, "flir")
    view_front = CameraView(root, axis_info, camera_available, "axis")
    #manual_button = BaseButton(root, button_manual_info, enable = True)
    #auto_button = BaseButton(root, button_auto_info, enable= False)
    #timer_canvas = TimerCanvas(root, timer_canvas_info)
    #yes_button = BaseButton(root, button_yes_info, activate=False)
    #no_button = BaseButton(root, button_no_info, activate = False)
    #start_button = BaseButton(root, button_start_info, activate=True)
    #score_canvas = ScoreCanvas(root, score_canvas_info)
    #jackal_ai = JackalAI()

    #return bar_canvas,danger_canvases,task_canvas,view_back,view_front,manual_button,auto_button, dialogue_text, yes_button, no_button, timer_canvas, #start_button, score_canvas

    return  view_back, view_front, dialogue_text

'''
def bind(root, cursor_canvas_small, cursor_canvas_big, bar_canvas, danger_canvases, task_canvas, view_back, view_front, manual_button, auto_button):
    root.bind('s', lambda e: switch(back = view_back, front = view_front, small=cursor_canvas_small, big=cursor_canvas_big))
    root.bind('x', lambda e: switch_auto(auto_button,manual_button))
    root.bind('w', lambda e: switch_danger(bar_canvas, danger_canvases))
    root.bind('`', lambda e: reset_bar(bar_canvas))
    root.bind('1', lambda e: reset_bar(danger_canvases[0]))
    root.bind('2', lambda e: reset_bar(danger_canvases[1]))
    root.bind('3', lambda e: reset_bar(danger_canvases[2]))
    root.bind('o', lambda e: task_canvas.plus())
    root.bind('a', lambda e: change_scan_mode())   
'''
def bind(root, cursor_canvas_small, cursor_canvas_big, view_back, view_front):
    root.bind('s', lambda e: switch(back = view_back, front = view_front, small=cursor_canvas_small, big=cursor_canvas_big))
    root.bind('a', lambda e: change_scan_mode())   

def change_scan_mode():
    CameraView.scan_mode = not CameraView.scan_mode
    print(CameraView.scan_mode)

def switch(back, front, small, big):

        if back.is_front == False:
            #Flir is front ,Axis is back
            front.update_pos(flir_info)
            back.update_pos(axis_info)
            small.enable()
            big.disable()
        else:
            #Axis is front,Flir is back
            front.update_pos(axis_info)
            back.update_pos(flir_info)
            small.disable()
            big.enable()

def reset_bar(bar):
    bar.reset_button()

def switch_danger(barcanvas, dangercanvases):
    if barcanvas.active:
        barcanvas.reset()
        barcanvas.disable()
        danger_enabled = [dangercanvas.reset() for dangercanvas in dangercanvases]
        danger_enabled = [dangercanvas.enable() for dangercanvas in dangercanvases]
        BarCanvas.danger_mode = True
    else:
        barcanvas.reset()
        barcanvas.enable()
        danger_disabled = [dangercanvas.reset() for dangercanvas in dangercanvases]
        danger_disabled = [dangercanvas.disable() for dangercanvas in dangercanvases]
        BarCanvas.danger_mode = False
       
def switch_auto(auto_button, manual_button):

    if auto_button.active:
        auto_button.disable()
        manual_button.enable()
    elif manual_button.active:
        auto_button.enable()
        manual_button.disable()

def server_program():
    hostname = socket.gethostname()
    print(hostname)
    # host = socket.gethostbyname('hp-green')
    # print(host)

    #server socket
    s = socket.socket()
    s.bind(('192.168.2.15',9999))
    s.listen(2)
    print("waiting for connection")
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024).decode()
        print(data)
        if not sound_mode: post_event("receive_command_text", data)
        else: post_event("receive_command_voice", data)
        print(data)

def play_sounds(data):
        if data == '1':
            playsound('/home/pouya/catkin_ws/src/test/src/sounds/left.mp3')
        elif data == '2':
            playsound('/home/pouya/catkin_ws/src/test/src/sounds/right.mp3')
        elif data == '3':
            playsound('/home/pouya/catkin_ws/src/test/src/sounds/stop.mp3')
        elif data == '4':
            playsound('/home/pouya/catkin_ws/src/test/src/sounds/go.mp3')
        else:
            playsound('/home/pouya/catkin_ws/src/test/src/sounds/back.mp3')

if __name__ == "__main__":
    main()