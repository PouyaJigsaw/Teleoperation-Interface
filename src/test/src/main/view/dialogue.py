from ast import If
from email.policy import default
from re import X
from tkinter import DISABLED, Label, Text
from event import *

social_dialogue_dict = {   
    "Start Q":
                        "Hey, I am Jackal!. Shall we start?",
    "Start A":
                                "Let's gooo!!!",
    "Danger State Start I":
                                "... I will handle it this time.",
    "Danger State End I":
                                "Uuh! I guess i did X mistakes while i added Y to the scores I lost Z score. I am sorry about this ... (Reason??)",
    "Danger State Start II Q":
                                "Hey I know I did wrong. But can you let me do it again? I try to do better this time.",
    "Danger State Start II A - Y":
                                "Thanks buddy! This time i try to do better.",
    "Danger State Start II A - N":
                                "I understand. Maybe next time.",
    "Danger State End II":
                                "Yay! I did it flawlessly I added X scores.",
    "End":
                                "It was nice working with you!"

       

}

nonsocial_dialogue_dict = {
    "Start Q":
                        "This is jackal ... preliminary training for search and rescue. Start the experiment?",
    "Start A":
                                "Preparing ...",
    "Danger State Start I":
                             "... Activating Assisted Mode",
    "Danger State End I":
                            "Number of faults: X\nReceived Score: Y\nLost Score: Z\nOverall: OO",
    "Danger State Start II Q":
                                "... Would you like to activate assisted mode?",
    "Danger State Start II A - Y":
                                "*(Updated) Assisted mode activated!",
    "Danger State Start II A - N":
                                "...",
    "Danger State End II":
                                "Number of faults: X\nReceived Score: Y\nLost Score: Z\nOverall: OO",
    "End":
                                "Thank you for using ..."

       

}

mega_dict = {
    "1": "Turn Left",
    "2": "Turn Right",
    "3": "Stop",
    "4": "Go Forward",
    "5": "Go Backward"
}
social_mode = False

dbox_info = {
    "x": 560,
    "y": 800,
    "width": 800,
    "height": 180
}


class DialogueBox():
    def __init__(self, root, dialoguebox_info, dialogues):
        self.x = dialoguebox_info["x"]
        self.y = dialoguebox_info["y"]
        self.width = dialoguebox_info["width"]
        self.height = dialoguebox_info["height"]
        self.state = "Start Q"
        self.dialogue = social_dialogue_dict[self.state] if social_mode is True else nonsocial_dialogue_dict[self.state]
        self.dialoguetext = Label(root, width= self.width, height= self.height,
                                font=('Calibri',12, 'bold', 'italic'),
                                bg='#e0de99')
        self.dialoguetext.config(text= self.dialogue)
        self.dialoguetext.place(x = self.x, y = self.y, width= self.width, height= self.height)
        print("created a dialogue box!")
        
        subscribe("receive_command_text", self.change_dialogue)

    def change_dialogue(self, string):
        print("here!_dialogue")
        self.state = string
        #self.dialogue = social_dialogue_dict[self.state] if social_mode is True else nonsocial_dialogue_dict[self.state]\
        self.dialogue = mega_dict[self.state]
        self.dialoguetext.config(text= self.dialogue)

    