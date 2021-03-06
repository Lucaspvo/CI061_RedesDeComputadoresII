#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Jean Carlos Maia
    Lucas Pazelo Vargas de Oliveira
    Servidor Portal TCP Iterativo Redes II """

import socket
import sys
sys.path.append( 'redes\ II' )
from Package import *
from Convert import *
from Log import *
from FileHandler import *
from Transmition import *
import random

numberServer = 0

""" Function to choose the process' server """
def schedulingChoice(uchoice):
    global numberServer
    if uchoice == 1:
    	PortalServerLog.logMessage(host + ": utilizado escalonamento Aleatório")
        return 2*(random.randint(1,(len(sys.argv)-2)/2))
    elif uchoice == 2:
        if numberServer == (len(sys.argv)-2)/2:
            numberServer = 0
        numberServer += 1
        PortalServerLog.logMessage(host + ": utilizado escalonamento Round-Robin")
        return 2*(numberServer)

""" Function that selects the process server """
def serverSelection(host, string, server, port):
    try:
        r = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        PortalServerLog.logMessage(host + ": criado socket para a conexão com o servidor de processamento: " + server + " na porta " + str(port))
    except socket.error, (errno, errmsg):
        PortalServerLog.logMessage("Erro ao criar socket: " + str( errno ) + ": " + str( errmsg ))
        sys.exit(1)
    ip = socket.gethostbyname(server)
    try:
        r.connect((ip, port))
        PortalServerLog.logMessage(host + ": estabelecida conexão com o servidor de processamento: " + server)
    except socket.error, ( errno, errmsg ):
        s.close()
        PortalServerLog.logMessage( "Erro ao realizar o connect(): " + str( errno ) + ": " + str( errmsg ) )
        sys.exit( 1 )
    try:
        Transmition.Send(r, string)
        PortalServerLog.logMessage(host + ": enviado arquivo fonte (do cliente) ao servidor de processamento: " + server)
    except socket.error, ( errno, errmsg ):
        s.close()
        PortalServerLog.logMessage( "Erro ao enviar a mensagem: " + str( errno ) + ": " + str( errmsg ) )
        sys.exit( 1 ) 
    PortalServerLog.logMessage(host + ": ------------------------------------------------------------------------------")
    PortalServerLog.logMessage(host + ": | esperando servidor de processamento: " + server + " retornar com a resposta |")
    PortalServerLog.logMessage(host + ": ------------------------------------------------------------------------------")
    try:
        string = Transmition.Recv(r)
        PortalServerLog.logMessage(host + ": recebida resposta da execução do servidor de processamento: " + server)
    except socket.error, ( errno, errmsg ):
        s.close()
        PortalServerLog.logMessage( "Erro ao receber a resposta: " + str( errno ) + ": " + str( errmsg ) )
        sys.exit( 1 ) 
    try:
        r.close()
        PortalServerLog.logMessage(host + ": socket de comunicação fechado")
    except socket.error, ( errno, errmsg ):
        s.close()
        PortalServerLog.logMessage( "Erro ao receber a resposta: " + str( errno ) + ": " + str( errmsg ) )
        sys.exit( 1 ) 
    return string    

""" Get local machine name """
host = socket.gethostname()

""" Create instance of Log Class """
PortalServerLog = Log( 'PortalServerLog_'+host+'.txt' );

""" Create package """
pack = Package()

""" Reserve a port for your service """
port = int (sys.argv[1])

""" Create a socket object """
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    PortalServerLog.logMessage(host + ": criado socket")
except socket.error, (errno, errmsg):
    PortalServerLog.logMessage("Erro ao criar socket: " + str( errno ) + ": " + str( errmsg ))
    sys.exit(1)

""" Bind to the port """
try:
    s.bind((host, port))
    PortalServerLog.logMessage(host +": realizado bind() na porta: " + str(port))
except socket.error, (errno, errmsg):
    s.close()
    PortalServerLog.logMessage("Erro ao realizar o bind(): " + str( errno ) + ": " + str( errmsg ))
    sys.exit(1)
    print
    print "Esperando por conexão!"
    
""" Now wait for client connection """
try:
    s.listen(10)
    PortalServerLog.logMessage(host + ": esperando por conexão")
except socket.error, (errno, errmsg):
    s.close()
    PortalServerLog.logMessage("Erro ao realizar o listen(): " + str( errno ) + ": " + str( errmsg ))
    sys.exit(1)

while True:
    PortalServerLog.logMessage("-------------------------------------------------------------------------------------------------------------")
    print
    print "Esperando por conexão!"
    """ Establish connection with client """
    try:
        sockRecv, remoteAddr = s.accept()
        PortalServerLog.logMessage(host + ": realizada conexão com cliente")
    except socket.error, (errno, errmsg):
        s.close()
        PortalServerLog.logMessage("Erro ao realizar o accept(): " + str( errno ) + ": " + str( errmsg ))
        sys.exit(1)
    
    """ Receive message from client """
    try:
        string = Transmition.Recv(sockRecv)
    except socket.error, (errno, errmsg):
        s.close()
        PortalServerLog.logMessage("Erro ao receber mensagem: " + str( errno ) + ": " + str( errmsg ))
        sys.exit(1)
    
    print
    print "Mensagem recebida do cliente!"
    
    """ Change the message from string to package """
    pack = Convert.StringToPackage(string)
    
    PortalServerLog.logMessage(host + ": recebida mensagem do cliente: " + pack.getNomeHost())
    
    """ Get the user's choice for random or Round-Robin server's choice """
    forward = schedulingChoice(int(pack.getServerChoice()))
    
    pack.setNomeServer(host)
    
    """ Change the message from package to string """
    string  = Convert.PackageToString(pack)
    
    """ Function to choose which process' server will be selected """
    string = serverSelection(host, string, sys.argv[forward], int(sys.argv[forward+1]))
        
    print
    print "Enviando mensagem de retorno ao cliente!"
    """ Send compilation result or error from the program execution to the client """
    try:
        Transmition.Send(sockRecv, string)
        PortalServerLog.logMessage( host + ": enviado resultado da execução para o cliente: " + pack.getNomeHost())
    except socket.error, ( errno, errmsg ):
        s.close()
        PortalServerLog.logMessage( "Erro ao enviar o resultado: " + str( errno ) + ": " + str( errmsg ) )
        sys.exit( 1 ) 

""" Close the connection """
sockRecv.close()


