'''
simple program to continuously plot a mag component to aid in magnetometer alignment
Bob Benedict   KD8CGH  10/15/2921
script reads latest line from log file and plots a value in Thonny plot window
expects plain tex log
uncomment component you want to plot
click in Thonny bottom window and choose "Show Plotter"
kill right side windows to expand plot window
'''
import os, time

#Set the filename and open the file
filename = 'KD8CGH-20211015-runmag.log'  #  insert your plain text log file name
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
        sline=line.split(",")
#        print(sline[3]) #  x
        print(sline[4]) # y
#        print(sline[5]) # z
        
