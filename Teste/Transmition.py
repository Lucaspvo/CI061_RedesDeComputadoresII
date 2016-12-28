#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import sys

class Transmition( object ):
    global END_OF_TRANSMITION
    global ACK
    END_OF_TRANSMITION = chr(4)
    ACK = chr(6)
    
    @staticmethod
    def Send(socket, string):
        socket.send(string)
        socket.send(END_OF_TRANSMITION)
        
    @staticmethod
    def Recv(socket):
        strg = ''
        while True:
            data = socket.recv(1480)
            if data[-1] != END_OF_TRANSMITION:
                strg += data
            else:
                strg += data[:-1]
                break
        return strg