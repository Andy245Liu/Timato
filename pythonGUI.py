# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 05:26:47 2020

@author: ptitf

"""
'''
import tkinter

from tkinter import *

top = tkinter.Tk()

class Window(Frame):

    root = Tk()
    #app = Window(root)
    root.wm_title("Timato")
    root.geometry("320x200")
    root.mainloop()



    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master

        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        # create Add Tasks button, link it to clickAddTasksButton()
        AddTasksButton = Button(self, text="Add Tasks", command=self.clickAddTasksButton)

        # create Delete Tasks button, link it to clickDelTasksButton()
        DelTasksButton = Button(self, text="Delete Tasks", command=self.clickDelTasksButton)

        # create Edit Tasks button, link it to clickEditTasksButton()
        EditTasksButton = Button(self, text="Edit Tasks", command=self.clickEditTasksButton)

        # create View Tasks button, link it to clickViewTasksButton()
        ViewTasksButton = Button(self, text="View Tasks", command=self.clickViewTasksButton)
        
        # create button, link it to clickExitButton()
        exitButton = Button(self, text="Exit", command=self.clickExitButton)
       
        # button locations
        AddTasksButton.place(x=100,y=100)
        DelTasksButton.place(x=300,y=100)
        EditTasksButton.place(x=500,y=100)
        ViewTasksButton.place(x=200,y=300)
        exitButton.place(x=400, y=300)
           
    def clickAddTasksButton(self):
        # declare the window
        window = Tk()
        # set window title
        window.title("Python GUI App")
        # set window width and height
        window.configure(width=500, height=300)
        # set window background color
        window.configure(bg='lightgray')
        window.mainloop()
    def clickDelTasksButton(self):
        pass
    def clickEditTasksButton(self):
        pass
    def clickViewTasksButton(self):
        pass
    def clickExitButton(self):
        exit()

    

    B = tkinter.Button(top, text ="Hello", command = clickAddTasksButton)
        
'''


###attempt 2
from operator import itemgetter
from datetime import datetime

import tkinter
from tkinter import *
from tkinter.ttk import *
import sqlite3
from sqlite3 import Error
conn = sqlite3.connect('Data.db')
c = conn.cursor()

class AddTaskWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()
        L1 = tkinter.Label(self, text="Name")
        L1.place(x=10, y  =50)
        self.nameField = Entry(self)
        self.nameField.place(x=200, y=50)
        L2 = tkinter.Label(self, text="Type (Static or Dynamic)")
        L2.place(x=10, y  =70)
        self.typeField = Entry(self)
        self.typeField.place(x=200, y=70)
        L3 = tkinter.Label(self, text="Weighting(1-10)")
        L3.place(x=10, y  =90)
        self.weightingField = Entry(self)
        self.weightingField.place(x=200, y=90)
        L4 = tkinter.Label(self, text="Mental Effort(1-10)")
        L4.place(x=10, y  =110)
        self.mentalEffortField = Entry(self)
        self.mentalEffortField.place(x=200, y=110)
        L5 = tkinter.Label(self, text="Deadline")
        L5.place(x=10, y  =130)
        self.deadlineField = Entry(self)
        self.deadlineField.place(x=200, y=130)
        L6 = tkinter.Label(self, text="Duration(minutes)")
        L6.place(x=10, y  =150)
        self.durationField = Entry(self)
        self.durationField.place(x=200, y=150)
        L7 = tkinter.Label(self, text="Screen Block (0 or 1)")
        L7.place(x=10, y  =170)
        self.screenBlockField = Entry(self)
        self.screenBlockField.place(x=200, y=170)
        L8 = tkinter.Label(self, text="Start Time")
        L8.place(x=10, y  =190)
        self.startTimeField = Entry(self)
        self.startTimeField.place(x=200, y=190)

        finalizeButton = Button(self, text="Submit", command= self.submit)

        # placing the button on my window
        finalizeButton.place(x=200, y=230)


        
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("Add Task")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)
    def getName(self):
        return self.nameField.get()
    def getType(self):
        return self.typeField.get()
    def getWeighting(self):
        return self.weightingField.get()
    def getMentalEffort(self):
        return self.mentalEffortField.get()
    def getDeadline(self):
        return self.deadlineField.get()
    def getDuration(self):
        return self.durationField.get()
    def getScreenBlock(self):
        return self.screenBlockField.get()
    def getStartTime(self):
        return self.startTimeField.get()
    def submit(self):
        task = []
        name = self.getName()
        task.append(name)
        typeTask = self.getType()
        task.append(typeTask)
        weighting = self.getWeighting()
        task.append(weighting)
        effort = self.getMentalEffort()
        task.append(effort)
        deadline = self.getDeadline()
        task.append(deadline)
        duration = self.getDuration()
        task.append(duration)
        block = self.getScreenBlock()
        task.append(block)
        startTime = self.getStartTime()
        task.append(startTime)
        print(task)
        c.execute("INSERT INTO Data(Name, Type, Weighting, MentalEffort,Deadline, Duration,ScreenBlock,StartTime) VALUES(?,?,?,?,?,?,?,?)", task)
        
        conn.commit()




       


class Window(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()
    def clickAddTasksButton(self):
        # declare the window
        
        a = Tk()
        a.geometry("400x300")
        appAdd = AddTaskWindow(a)
        
   
        a.mainloop()     


    #Creation of init_window

    def init_window(self):

        # changing the title of our master widget      
        self.master.title("Home")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        quitButton = Button(self, text="Add Task", command=self.clickAddTasksButton)

        # placing the button on my window
        quitButton.place(x=50, y=50)
   
        

root = Tk()

#size of the window
root.geometry("400x300")

app = Window(root)
root.mainloop()  

'''

# This will import all the widgets 
# and modules which are available in 
# tkinter and ttk module 
from tkinter import * 
from tkinter.ttk import *
  
# creates a Tk() object 
master = Tk() 
  
# sets the geometry of main  
# root window 
master.geometry("200x200") 
  
  
# function to open a new window  
# on a button click 
def openNewWindow(): 
      
    # Toplevel object which will  
    # be treated as a new window 
    newWindow = Toplevel(master) 
  
    # sets the title of the 
    # Toplevel widget 
    newWindow.title("New Window") 
  
    # sets the geometry of toplevel 
    newWindow.geometry("200x200") 
  
    # A Label widget to show in toplevel 
    Label(newWindow,  
          text ="This is a new window").pack() 
    w = Entry()
    w.place(x=50, y=50)
  
  
label = Label(master,  
              text ="This is the main window") 
  
label.pack(pady = 10) 
  
# a button widget which will open a  
# new window on button click 
btn = Button(master,  
             text ="Click to open a new window",  
             command = openNewWindow) 
btn.pack(pady = 10) 
  
# mainloop, runs infinitely 
mainloop() 
'''


