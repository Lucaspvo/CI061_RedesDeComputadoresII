#!/usr/bin/env python
# -*- coding: utf-8 -*-

class FileHandler( object ):
        
        FilePointer = None
        
        """ Class Constructor 
               @param self Object Pointer """
        def __init__( self ):
                self.FilePointer = None
        
        """ Open a file 
               @param self Object Pointer
               @param filename File's name
               @param mode Mode to open a file """
        def open( self, filename, mode ):
                self.FilePointer = open( filename, mode)
        
        """ Write a message in a file
                @param self Object Pointer
                @param msg Message to be written in the file """
        def write( self, msg ):
                self.FilePointer.write( msg )
                
        """ Read from a file 
                @param self Object Pointer 
                @return Return all the lines from the file"""
        def read( self ):
                return self.FilePointer.read()
        
        """ Read a line from a file 
               @param self Object Pointer
               @return Return one line at a time """
        def readline( self ):
                return self.FilePointer.readline().rstrip()
        
        """ Read all lines from a file 
               @param self Object Pointer
               @return Return the content """
        def readlines( self ):
                return self.FilePointer.readlines()

        """ Close file 
               @param self Object Pointer """
        def close( self ):
                self.FilePointer.close()