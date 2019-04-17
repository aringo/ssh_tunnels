#! /usr/bin/python3

import sys
import time 
import socket


host =sys.argv[1]
port =8080
Flag="3af7917703e3888de707119691d70c16"
SleepTime=15
while 1:
    try:
        #print("Connecting to send Flag")
        s = socket.socket()
        s.connect((host,port))
        s.send(Flag.encode()) 
        s.close() 
    except:
        #print("No Connection Made")
        pass
    #print("Sleeping for {}".format(SleepTime))
    time.sleep( SleepTime )
