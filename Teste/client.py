#!/usr/bin/python           # This is client.py file
# -*- coding: utf-8 -*-
import socket               # Import socket module               
import sys
sys.path.append( 'Teste' )
from Transmition import *



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.connect((host, port))
data = "Vou me comunicar com o servidor agora!"
Transmition.Send(s, data)
#s.recv(1480)
data = "Ja devia ter parado"
Transmition.Send(s, data)
string = Transmition.Recv(s)
print string
s.close                     # Close the socket when done
