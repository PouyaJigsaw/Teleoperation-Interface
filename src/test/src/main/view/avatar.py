from tkinter import Label
from PIL import Image, ImageTk
import time
import threading
import event
from dialogue import social_mode


javatar_info = {
    "x": 460,
    "y": 800,
    "width": 200,
    "height": 180,
}


javatar_images = {
    "default" : "/home/pouya/catkin_ws/src/test/src/images/default.png",
    "default-talking": "/home/pouya/catkin_ws/src/test/src/images/default-talking-placeholder.png",
    "default-blink": "src/test/src/images/default-blink-placeholder.png",
    "happy" : "/home/pouya/catkin_ws/src/test/src/images/happy.png",
    "happy-blink": "/home/pouya/catkin_ws/src/test/src/images/happy-blink-placeholder.png",
    "sad" : "/home/pouya/catkin_ws/src/test/src/images/sad.png",
    "sad-blink": "/home/pouya/catkin_ws/src/test/src/images/sad-blink-placeholder.png",
    "angry": "/home/pouya/catkin_ws/src/test/src/images/angry.png",
    "angry-blink": "/home/pouya/catkin_ws/src/test/src/images/angry-blink-placeholder.png",
    "nonsocial": "/home/pouya/catkin_ws/src/test/src/images/non_social_avatar.jpg"

}


class Avatar():
    
    def __init__(self,root , avatar_info, avatar_images):
            self.x = avatar_info["x"]
            self.y = avatar_info["y"]
            self.width = avatar_info["width"]
            self.height = avatar_info["height"]
            self.image = Image.open(avatar_images["default"]).resize((self.width,self.height), Image.ANTIALIAS) if social_mode is True else Image.open(avatar_images["nonsocial"]).resize((self.width,self.height), Image.ANTIALIAS)
            self.imagetk = ImageTk.PhotoImage(self.image)
            self.label = Label(root)
            self.label.config(image = self.imagetk)
            self.label.image = self.imagetk
            self.label.place(x = self.x ,y = self.y ,width = self.width ,height = self.height)
            self.state = "default"

            
            if social_mode:
                event.EventManager.subscribe("collision", self.change_image_hit)
                event.EventManager.subscribe("mistake", self.change_image_hit)
                event.EventManager.subscribe("congratulations", self.change_image_congratulations)


    def change_image(self,state):
        self.image = Image.open(javatar_images[state]).resize((self.width,self.height), Image.ANTIALIAS)
        self.state = state
        self.imagetk = ImageTk.PhotoImage(self.image)
        self.label.config(image = self.imagetk)
        self.label.image = self.imagetk

    def change_image_temp(self,state):
        def swap_images(s, p_s):
            self.change_image(s)
            time.sleep(10)
            self.change_image(p_s)
        prev_state = self.state
        t = threading.Thread(target=swap_images, args=(state, prev_state))
        t.start()

    def change_image_hit(self, dummy):
        def swap_images(s, p_s):
            self.change_image(s)
            time.sleep(4)
            self.change_image(p_s)
        prev_state = self.state
        t = threading.Thread(target=swap_images, args=("angry", prev_state))
        t.start()
        
      
    def change_image_congratulations(self, dummy):
        def swap_images(s, p_s):
            self.change_image(s)
            time.sleep(7)
            self.change_image(p_s)
        prev_state = self.state
        t = threading.Thread(target=swap_images, args=("happy", prev_state))
        t.start()

        
        
