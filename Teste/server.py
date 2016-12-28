#!/usr/bin/python           # This is server.py file
# -*- coding: utf-8 -*-
import socket               # Import socket module
import time
import errno              
import sys
sys.path.append( 'Teste' )
from Transmition import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
    c, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    string = Transmition.Recv(c)
    print string
    #c.send("ACK")
    strg = Transmition.Recv(c)
    print strg
    strg = 'Thank you for connecting'
    Transmition.Send(c, strg)
    c.close()                # Close the connection



"""while True:
        try:
            data = c.recv(2)
        except socket.error, e:
            err = e.args[0]
            if err != errno.EAGAIN or err != errno.EWOULDBLOCK:
                print "if"
                break
        string += data"""