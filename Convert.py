#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle 
import sys



class Convert( object ):
        
        """ Transform a string received into a package to be used """
        @staticmethod
        def StringToPackage( string ):
                pack = pickle.loads( string )
                return pack
        
        """ Transform a package into a string to be sent """
        @staticmethod
        def PackageToString( pack ):
                string = pickle.dumps( pack )
                return string