#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
def usersChoice(uchoice):
    print "entrei ---> " + str(uchoice)
    print
    global numberServer
    if uchoice == 1:
        rad = random.randint(1,3)
        print rad
        print
        return rad
    elif uchoice == 2:
        print "Round-Robin"
        print
        if numberServer == 3:
            numberServer = 0
        numberServer += 1
        return numberServer
    
numberServer = 0
c = int(raw_input())
v = usersChoice(c)
print v