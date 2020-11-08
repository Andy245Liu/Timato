# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 01:52:56 2020

@author: ptitf
"""

import sqlite3


conn = sqlite3.connect('Data.db')

print("Opened database successfully")

def add(): #add activity to the DB

    conn = sqlite3.connect('Data.db')

    L = []
    activityName = input("Enter a name please.")
    L.append(activityName)
    activityType = input("Is this a routinely activity or a one-time activity? \
                         Please enter Static or Dynamic accordingly.")
    L.append(activityType)
    activityWeighting = input("How important is this activity from 1 to 10?")
    L.append(activityWeighting)
    activityMental = input("How mentally challenging is this activity from 1 to 10?")
    L.append(activityMental)
    activityDeadline = input("When is this activity due? Please enter a date \
                             in the following format: YYYY-MM-DD HH:MM:SS")
    L.append(activityDeadline)
    activityDuration = input("How long does this activity take? (in minutes)")
    L.append(activityDuration)
    activityScreen = input("Would you like to benefit from the Screen Block \
                           feature? (have forced breaks once every 25 minutes) Please enter 0 for no and 1 for yes.")
    L.append(activityScreen)
    if activityType == "Static":
        activityStartTime = input("When will you start this activity? Please enter a date \
                             in the following format: YYYY-MM-DD HH:MM:SS")
    else:
        activityStartTime = "1999-01-01 00:00:00"
    L.append(activityStartTime)
                             
                             
    conn.execute("INSERT INTO DATA (NAME,TYPE,WEIGHTING,MENTALEFFORT,DEADLINE,\
                 DURATION,SCREENBLOCK,STARTTIME) \
      VALUES ('" + L[0] + "', '" + L[1] + "', " + L[2] + ", " + L[3] + ", '" + L[4] + "', " + L[5] + ", " + L[6] + ", '" + L[7] + "')")
    
    conn.commit()
    print("Activity created successfully")
    conn.close()
    
def view(): # view activities in the DB
    
    conn = sqlite3.connect('Data.db')

    cursor = conn.execute("SELECT NAME,TYPE,WEIGHTING,MENTALEFFORT,DEADLINE,\
                 DURATION,SCREENBLOCK,STARTTIME from DATA")
    for row in cursor:
       print("NAME= ", row[0])
       print("TYPE = ", row[1])
       print("WEIGHTING = ", row[2])
       print("MENTALEFFORT = ", row[3], "\n")
       print("DEADLINE = ", row[4], "\n")
       print("DURATION = ", row[5], "\n")
       print("SCREENBLOCK = ", row[6], "\n")
       print("STARTTIME = ", row[7], "\n")
       
    print("Operation done successfully")
    conn.close()
    
def edit(): #edit activities in the DB
    
    conn = sqlite3.connect('Data.db')

    whichActivity = input("Which activity would you like to edit?")
    whichFeature = input("Which feature would you like to edit? Enter 0 to stop editing.")
    if whichFeature != '0':
        whichValue = input("Please enter a new value, using the appropriate syntax.")
            
    while whichFeature != '0':
        if whichFeature == 'Weighting' or whichFeature == 'Name' or whichFeature == 'Type' or whichFeature == "Deadline" or whichFeature == 'StartTime':
            conn.execute("UPDATE DATA set " + whichFeature + " = '" + whichValue + "' where NAME = '" + whichActivity + "'")
        else:
            conn.execute("UPDATE DATA set " + whichFeature + " = " + whichValue + " where NAME = '" + whichActivity + "'")

        whichFeature = input("Which feature would you like to edit? Enter 0 to stop editing.")
        if whichFeature == '0':
            break
        whichValue = input("Please enter a new value, using the appropriate syntax.")
        
    conn.commit()
    print("Total number of rows edited :", conn.total_changes)
    
    view()
    
    
def delete(): #delete activities in the DB
    
    conn = sqlite3.connect('Data.db')

    whichActivity = input("Which activity would you like to edit?")

    conn.execute("DELETE FROM DATA WHERE NAME = '" + whichActivity + "'")
    conn.commit()
    print("Total number of activities deleted :", conn.total_changes)
    
    view()