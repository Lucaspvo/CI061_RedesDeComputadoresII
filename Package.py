#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Package( object ):
    serverChoice  = None 
    fileName      = None
    nomeHost        = None
    nomeServer      = None
    dados         = None
    
    """ Class Constructor
        @param self Object Pointer
        @param sChoice Client's choice for a method to choose a process' server
        @param fName File's name
        @param host Host's name
        @param server Server's name
        @param dados Data (client's file data) """
    def __init__( self, sChoice = None, fName = None, host = None, server = None, dados = None ):
        self.serverChoice = sChoice
        self.fileName = fName
        self.nomeHost = host
        self.nomeServer = server
        self.dados = dados
        
    """ Set User's choice for the Process Server """
    def setServerChoice( self , sChoice):
        self.serverChoice = sChoice
    
    """ Set User's File Name """
    def setFileName( self, fName ):
        self.fileName = fName
    
    """ Set Host's Name """
    def setNomeHost( self, host ):
        self.nomeHost = host
    
    """ Set Server's Name """
    def setNomeServer( self, server ):
        self.nomeServer = server
    
    """ Set the data (client's file data) """
    def setDados( self, dados ):
        self.dados = dados
    
    """ Get User's choice for the Process Server """
    def getServerChoice( self ):
        return self.serverChoice
    
    """ Get User's File Name """
    def getFileName( self ):
        return self.fileName
    
    """ Get Host's Name """
    def getNomeHost( self ):
        return self.nomeHost
    
    """ Get Server's Name """
    def getNomeServer( self ):
        return self.nomeServer
    
    """ Get the data (client's file data) """
    def getDados( self ):
        return self.dados