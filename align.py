'''
simple program to continuously plot a mag component to aid in magnetometer alignment
Bob Benedict   KD8CGH  10/15/2921
script reads latest line from log file and plots a value in Thonny plot window
set filename to log file log
uncomment component you want to plot
click in Thonny bottom window and choose "Show Plotter"
kill right side windows to expand plot window
'''
import os, time

#Set the filename and open the file
filename = 'KD8CGH-20211025-runmag.log'  #  insert your plain text log file name
file = open(filename, 'r', encoding = 'utf-8')

#Find the size of the file and move to the end
st_results = os.stat(filename)
st_size = st_results[6]
file.seek(st_size)

while 1 :
    where = file.tell()
    line = file.readline()
    if not line:
        time.sleep(1)
        file.seek(where)
    else:
        
        if line[0] == '{':   # json file
            ls=line.split(':')
#            lsl=ls[6]
#            print(lsl.split(',')[0])  # x            
            lsl=ls[7]
            print(lsl.split(',')[0])  # y
#            lsl=ls[8]
#            print(lsl.split(',')[0])  # z
         
        else:   # plain text file
            ls1=line.split(',')
#            print(ls1[3]) # x
            print(ls1[4]) # y
#            print(ls1[5]) # z

        
