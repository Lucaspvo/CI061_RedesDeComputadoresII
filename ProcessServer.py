#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Jean Carlos Maia
    Lucas Pazelo Vargas de Oliveira
    Servidor Processamento TCP Iterativo Redes II """

import socket
import sys
import os
import commands
import subprocess
sys.path.append( 'redes\ II' )
from Package import *
from Convert import *
from Log import *
from FileHandler import *
from Transmition import *

if len(sys.argv) != 2:
    print "Uso correto: %s <porta>" % sys.argv[0]
    sys.exit(1)

""" Get local machine name """
host = socket.gethostname()

""" Create instance of Log Class """
ProcessServerLog = Log( "ProcessServerLog_" + host + ".txt" );

filep = FileHandler()

""" Create a socket object """
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    ProcessServerLog.logMessage(host + ": criado socket")
except socket.error, (errno, errmsg):
    ProcessServerLog.logMessage("Erro ao criar socket: " + str( errno ) + ": " + str( errmsg ))
    sys.exit(1)

""" Reserve a port for your service """
port = int (sys.argv[1])

""" Bind to the port """  
try:
    s.bind((host, port))
    ProcessServerLog.logMessage(host + ": realizado bind() na porta: " + str(port))
except socket.error, (errno, errmsg):
    s.close()
    ProcessServerLog.logMessage("Erro ao realizar o bind(): " + str( errno ) + ": " + str( errmsg ))
    sys.exit(1)        

print "Esperando por conexão!"
""" Now wait for client connection """
try:
    s.listen(10)
    ProcessServerLog.logMessage(host + ": esperando por conexão (listen())")
except socket.error, (errno, errmsg):
    s.close()
    ProcessServerLog.logMessage("Erro ao realizar o listen(): " + str( errno ) + ": " + str( errmsg ))
    sys.exit(1)

while True:
    ProcessServerLog.logMessage("-------------------------------------------------------------------------------------------------------------")
    """ Establish connection with client """
    try:
        sockRecv, remoteAddr = s.accept()
        ProcessServerLog.logMessage(host + ": estabelecida conexão com servidor portal")
    except socket.error, (errno, errmsg):
        s.close()
        ProcessServerLog.logMessage("Erro ao realizar o accept(): " + str( errno ) + ": " + str( errmsg ))
        sys.exit(1)
    print "Estabelecendo conexão com servidor portal!"
    
    print "Recebendo mensagem!"    
    """ Receive message """
    try:
        string = Transmition.Recv(sockRecv)
        #ProcessServerLog.logMessage(host + ": recebida mensagem")
    except socket.error, (errno, errmsg):
        s.close()
        ProcessServerLog.logMessage("Erro ao receber a mensagem: " + str(errno) + ": " + str(errmsg))
        sys.exit(1)
    
    """ Convert the string received into package """
    pack = Package()
    pack = Convert.StringToPackage(string)
    
    ProcessServerLog.logMessage(host + ": recebido arquivo fonte (" + pack.getFileName() + ") do servidor portal: " + pack.getNomeServer())
    
    """ Open and write the program in server """
    filep.open(str(pack.getFileName()), 'w')
    filep.write(pack.getDados())
    filep.close()
    ProcessServerLog.logMessage(host + ": criado arquivo fonte (" + str(pack.getFileName()) + ") do cliente: " + pack.getNomeHost())
    
    print "Compilando e executando arquivo fonte!"
    """ Execute the program """
    process = subprocess.Popen(['python',str(pack.getFileName())], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    """ out -> the result of the execution of the program
        err -> error from the compilation """
    out, err = process.communicate()
    """ errcode -> a code used to distinguish the output, if it is the result or the error """
    errcode = process.returncode
    
    ProcessServerLog.logMessage(host + ": arquivo fonte compilado e executado")
    
    if errcode == 0:
        pack.setDados(out)
        pack.setNomeServer(host)
    else:
        pack.setDados(err)
        pack.setNomeServer(host)
    
    server = pack.getNomeServer()
    
    """ Convert the package into string """
    string = Convert.PackageToString(pack)
    
    print "Enviando resultado da execução!"
    """ Send the result to portal server """
    try:
        Transmition.Send(sockRecv, string)
        ProcessServerLog.logMessage(host + ": enviada resposta de execução ao servidor portal: " + server)
    except socket.error, (errno, errmsg):
        s.close()
        ProcessServerLog.logMessage("Erro ao enviar a mensagem: " + str(errno) + ": " + str(errmsg))
        sys.exit(1)
    
""" Close socket """
sockRecv.close()                                                           

