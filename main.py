from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
import customtkinter as ctk

import pyautogui as pg
# for copying and pasting questions
import pyperclip 
import time

import pygame
def close_window():
    if messagebox.askyesno(title="Exit",message="Are you sure, you want to exit?",icon = "info"):
        window.destroy()

    else:
        print("Keep it up!")

def create_note():
    noteWindow = Tk()
    noteWindow.title("NOTE ME:")
    noteWindow.geometry("300x200+250+250")

    note = Text(noteWindow,
            bg = "Black",
            font=("Ink Free",15),
            height=20,
            width=20,
            fg ="white" )
    note.pack()


# HERE we cannot remove hash and \n
def giveIndividualQuestion(questionBank):
    count = 1
    question_dict = {}
    line0 = []

    for line in questionBank:
        if "#" in line:
            # we could find index of # to make it seperate questions on same line but 

            question_dict[count] = "".join(line0) + line
            line0 = []
            count += 1
        else: line0.append(line)

    # If there's any leftover content in line0 (in case no '#' is in the last question)
    if line0:
        question_dict[count] = ''.join(line0)
    return question_dict


def openChatGPT():
    pg.hotkey('alt', 'tab')
    time.sleep(3)
    pg.hotkey('ctrl', 't')
    time.sleep(3)
    pg.moveTo(373, 137)
    time.sleep(3)
    pg.click()
    pg.press('a')
    pg.press('backspace')
    time.sleep(2)

def CopyPasteThing(thing):
    pyperclip.copy(thing)
    pg.moveTo(1000,700)
    time.sleep(0.2)
    pg.click()
    pg.press('a')
    pg.press('backspace')
    typing_sound.play()
    time.sleep(0.4)
    pg.hotkey('ctrl', 'v')
    pg.hotkey('backspace')

def submitChatGPT():
    # pg.press('tab')
    # pg.press('tab')
    # pg.press('tab')
    # pg.press('tab')
    # time.sleep(2)
    # pg.press('tab')
    time.sleep(0.5)
    pg.press('enter')
    glass_clink.play()


def nextQuestionButton():
    global index
    index +=1
    currentQuestion = f"{index}).{questions[index]}"
    button_click_sound.play()
    CopyPasteThing(currentQuestion)
    time.sleep(0.2)
    submitChatGPT()
    update_ProgressBar()

def previousQuestionButton():
    global index
    index-=1
    currentQuestion = f"{index}).{questions[index]}"
    button_click_sound.play()
    CopyPasteThing(currentQuestion)

def calculate1Percent():
    global questions, oneQuestionPercent
    maxno = len(questions)
    oneQuestionPercent = ((1/(maxno+1))*100)

def update_ProgressBar():
    global oneQuestionPercent,currentPercent,window,progress_label
    currentPercent += oneQuestionPercent
    progress_bar.set(currentPercent/100)
    progress_label.configure(text=f"{round(currentPercent,1)}%")
    window.update(window)
    





# Initialize pygame mixer for sound playback
pygame.mixer.init()
# Load sound file
button_click_sound = pygame.mixer.Sound('Personal python projects//QuestionBank answer finder//Manual extraction//normalclick.mp3')
typing_sound = pygame.mixer.Sound('Personal python projects//QuestionBank answer finder//Manual extraction//keyboardtyping.mp3')
glass_clink = pygame.mixer.Sound('Personal python projects//QuestionBank answer finder//Manual extraction//glassclink.mp3')
questionBank = open("c://Users//hp//Desktop//python//learn python//Personal python projects//QuestionBank answer finder//Manual extraction//testquestions.txt")

index = 0
oneQuestionPercent = 0
currentPercent = 0
questions = giveIndividualQuestion(questionBank)
print(f"Seperated questions: {questions}")

openChatGPT()
calculate1Percent()


# Basic parameters and initializations
# Supported modes : Light, Dark, System
ctk.set_appearance_mode("System") 

# Supported themes : green, dark-blue, blue
ctk.set_default_color_theme("dark-blue")   

# window length and breadth
windowLength = 300
windowBreadth = 100
window = ctk.CTk() # instantiate an instance of a window

uparrow = PhotoImage(file='Personal python projects\\QuestionBank answer finder\\Manual extraction\\greenBall.png')
stopBall = PhotoImage(file='Personal python projects\\QuestionBank answer finder\\Manual extraction\\redBall.png')

window.configure(background= "#ccd9ff")
window.geometry(f"{windowBreadth}x{windowLength}+1600+350")
window.attributes ('-topmost', True)
window.title("Control Panel")

# Remove title bar (no minimize, maximize, close buttons or icon)
#window.overrideredirect(True)
# canvas = ctk.CTkCanvas(window, width=100, height=100)
# canvas.place(x=10,y=150)

# canvas.create_line(20,20,20,60,width=2,fill="green")


# close_window_Button = ctk.CTkButton(window, text= "x",command= close_window,height=15,width=15,corner_radius=7,  fg_color="#007BFF",hover_color="#0056b3",text_color="white",font=("Segoe UI", 16, "bold"))
# close_window_Button.place(x=90,y=0)


next_Question_button =ctk.CTkButton(window,
                              image= uparrow,
                              text="",
                              height=20,
                              width=20,
                              corner_radius=10,
                              command=nextQuestionButton)
next_Question_button.grid(row=1,column=0,padx=10,pady=5)


stop_Question_button = ctk.CTkButton(window,
                              image= stopBall,
                               text="",
                              height=20,
                              width=20,
                              corner_radius=50,
                              command=previousQuestionButton)
stop_Question_button.grid(column=0,row=3,padx=10,pady=5)


note_button = ctk.CTkButton(window,
                     text="Note",
                     height=20,width=20,corner_radius=50,
                     command=create_note)
note_button.grid(column=0,row=5,padx=10,pady=10)

progress_bar = ctk.CTkProgressBar(window,width=100,height=15)
progress_bar.set(0)
progress_bar.grid(column=0,row=7,pady=0,padx=5)


progress_label = ctk.CTkLabel(window, text="0%")
progress_label.grid(column=0, row=6,pady=2)

window.mainloop() # place window on the screen and even listner
