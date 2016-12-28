#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import sys

""" Class created for transmition      Transmition() """
class Transmition( object ):
    global END_OF_TRANSMITION
    END_OF_TRANSMITION = chr(4)
    
    """ Send's first the data and by the end the END_OF_TRANSMITION """
    @staticmethod
    def Send(socket, string):
        socket.send(string)
        socket.send(END_OF_TRANSMITION)
    
    """ Receive's the data and when receive a END_OF_TRANSMITION it means that is the
        end of the package and send back the string without the character END_OF_TRANSMITION """
    @staticmethod
    def Recv(socket):
        strg = ''
        while True:
            data = socket.recv(1024)
            if data[-1] != END_OF_TRANSMITION:
                strg += data
            else:
                strg += data[:-1]
                break
        return strg