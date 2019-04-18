#! /usr/bin/python3

import sys
import time 
import socket


host =sys.argv[1]
port =8080
Flag="FLAG:YOU WIN!"
SleepTime=15
BUFFER_SIZE = 1024
msg = b"Send back the word - Please\n" 
while 1:  
    try:
        #print("Connecting to send Flag")
        s = socket.socket()
        s.connect((host,port))
        s.send(msg)
        data = s.recv(BUFFER_SIZE)
        if b"Please" in data:
            s.send(Flag.encode()) 
        s.close() 
    except:
        #print("No Connection Made")
        pass
    #print("Sleeping for {}".format(SleepTime))
    time.sleep( SleepTime )
