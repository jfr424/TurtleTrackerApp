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
    print(f"Record {record_id} indicated Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")
    date_dict[record_id] = obs_date
    coord_dict[record_id] = (obs_lat,obs_lon)