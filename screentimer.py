from datetime import datetime
import sqlite3
import sys
import time
import pyautogui
if sys.version_info[0] == 2:
    import Tkinter
    tkinter = Tkinter
else:
    import tkinter
from PIL import Image, ImageTk
first = 0
first2 = 0
#python C:\Users\Ahmad\Desktop\disptest.py

conn = sqlite3.connect('Data.db')
cursor = conn.execute("SELECT Name, Type, Weighting, MentalEffort, Deadline, Duration, ScreenBlock, StartTime from data")   # SQL DB Imported


Name = []
Type = []
Weight = []
Mental = []
Deadline = []
Duration = []
Block = []
StartTime = []
for row in cursor:
    Name.append(row[0])  # STR
    Type.append(row[1])  # STR
    Weight.append(row[2]) #INT
    Mental.append(row[3]) # INT
    Deadline.append(row[4]) # STR
    Duration.append(row[5]) # INT
    Block.append(row[6]) # INT
    StartTime.append(row[7]) # STR
   # print "ID = ", row[0]
   # print "NAME = ", row[1]
   # print "ADDRESS = ", row[2]
   # print "SALARY = ", row[3], "\n"

def findact(h, m, hour, minute, dur):
    for i in range(len(h)):
        timestart = h[i] * 60 + m[i]
        timeend = timestart + dur[i]
        if((hour*60 + minute) >= timestart and (hour*60 + minute) < timeend):
            return i
    return 1000

def checkassign(hour,minute, Deadline):
    for i in range(len(Deadline)):
        temp = Deadline[i].find(":")
        temptime = int(Deadline[i][temp-2])*600 + int(Deadline[i][temp-1]) * 60 + int(Deadline[i][temp+1]) * 10 + int(Deadline[i][temp+2])
        if(temptime - (hour*60+minute) <= 30 and temptime - (hour*60+minute) >= 0):
            return True
    return False

minlist = []
hourlist = []
dur = []
for i in range(len(StartTime)):
    a = StartTime[i]
    temp = a.find(":")
    minlist.append(int(a[temp+1]) * 10 + int(a[temp+2]))
    hourlist.append(int(a[temp-2]) * 10 + int(a[temp-1]))
    dur.append(int(Duration[i]))


#INSIDE LOOP
while True:
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    temp = dt_string.find(":")
    hour = 0
    minute = 0
    hour = int(dt_string[temp-2]) * 10 + int(dt_string[temp-1])
    minute = int(dt_string[temp+1]) * 10 + int(dt_string[temp+2])
    overall = hour*60 + minute
    breaktimes = []
    a = findact(hourlist, minlist, hour, minute, dur)
    if (a!= 1000):
        if(Block[a] == 1 and checkassign(hour, minute, Deadline) == False):
            freq = int(100/Mental[a])
            breakt = int(10/Mental[a])
            sum = 0
            x = 0
            while(sum < dur[i]):
                breaktimes.append((hourlist[a] * 60 + minlist[a]) + freq*(x+1) + breakt * x)
                sum+=freq*(x+1) + breakt * x
                x+=1
            for k in range(len(breaktimes)):
                if(breaktimes[k] <= overall and overall < breaktimes[k] + breakt):
                    if(first == 0):
                        pyautogui.keyDown('alt')
                        pyautogui.press('tab', presses=2)
                        pyautogui.keyUp('alt')
                        first += 1
                    else:
                        pyautogui.hotkey('alt', 'tab')
                    time.sleep(0.1)
                    pyautogui.hotkey('ctrl', 'shift', 'e')
                    time.sleep(60*breakt)
                    pyautogui.hotkey('shift', 'a')
                    break
    time.sleep(60)
# for i in range(2):
#     if(first == 0):
#         pyautogui.keyDown('alt')
#         pyautogui.press('tab', presses=2)
#         pyautogui.keyUp('alt')
#         first += 1
#     else:
#         pyautogui.hotkey('alt', 'tab')
#     time.sleep(0.1)
#     pyautogui.hotkey('ctrl', 'shift', 'e')
#     time.sleep(10)
#     pyautogui.hotkey('shift', 'a')
#     time.sleep(10)
