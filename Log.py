#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from datetime import datetime
sys.path.append( 'redes\ II' )
from FileHandler import *

""" Log's Class """
class Log( object ):
        
        """ Constructor """
        def __init__( self, logFileName ):
                self.logFileName = logFileName
        
        """ Add the next step to the Log's file
         @param self Object poiter
         @param msg Message to be written into the Log's file"""
        def logMessage( self, msg ):
                # Pega data e hora locais
                instantDate = datetime.now()
                
                hora = str('{0:02}'.format(instantDate.hour))
                minuto = str('{0:02}'.format(instantDate.minute))
                segundo = str('{0:02}'.format(instantDate.second))
                Log = FileHandler()
                Log.open( self.logFileName, 'a' )
                Log.write(hora + ":" + minuto + ":" + segundo + " ----> " + msg + '\n')
                Log.close()