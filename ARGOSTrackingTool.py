# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 16:16:21 2021

@author: jr424
"""
#ARGOSTrackingTool.py
#Description: Reads in an ARGOS file and allows user to view the location of a turtle
#Author: Juan Rebellon
#Date: Fall 2021
#Create a variable point to the data file

user_date = input("Enter date to search for Sara: ")

file_name = './data/sara.txt'

#Create a file object from the file
file_object = open(file_name,'r')

#Read contents of file into a list
line_list = file_object.readlines()

#Close the file
file_object.close()

#Create two empty dictionaries
date_dict = {}
coord_dict = {}

#Iterate through all lines in linelist
for lineString in line_list:
    if lineString[0] in ("#",'u'): continue

    #Split the string into a list of data items
    lineData = lineString.split()
    
    #Extract the items in list into variables
    record_id = lineData[0]  # ARGOS tracking record ID
    obs_date = lineData[2]   # Observation date
    ob_lc = lineData[4]      # Observation Location Class
    obs_lat = lineData[6]    # Observation Latitude
    obs_lon = lineData[7]    # Observation Longitude
    
    #Print the location of sara
    if ob_lc in ("1", "2", "3"):
        print(f"Record {record_id} indicated Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")
        date_dict[record_id] = obs_date
        coord_dict[record_id] = (obs_lat,obs_lon)
        
matching_keys = []

#Loop through items in the date_dict and collect keys for matching ones
for date_item in date_dict.items():
    #Get the date if the item
    the_key, the_date = date_item
    #See if the date matches the user date
    if the_date == user_date:
        matching_keys.append(the_key)
        
#Reveal locations for each key in matching keys
for matching_key in matching_keys:
    obs_lat, obs_lon = coord_dict[matching_key]
    print(f"Record {matching_key} indicated Sara was seen at lat:{obs_lat},lon:{obs_lon} on {user_date}")