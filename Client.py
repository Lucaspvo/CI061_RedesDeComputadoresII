#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Jean Carlos Maia
    Lucas Pazelo Vargas de Oliveira
    Cliente TCP Iterativo Redes II """

import socket               
import sys
sys.path.append( 'redes\ II' )
from Package import *
from Convert import *
from Log import *
from FileHandler import *
from Transmition import *

""" Name of the local machine """
host = socket.gethostname()

""" Create instance of Log Class """
ClientLog = Log( 'ClientLog_'+host+'.txt' );

""" Create a socket object """
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    ClientLog.logMessage( "Foi criado o socket no cliente: " + host)
except socket.error, ( errno, errmsg ):
    ClientLog.logMessage( "Erro ao criar socket: " + str( errno ) + ": " + str( errmsg ) )
    sys.exit( 1 )

""" Check for the right input """
if len(sys.argv) != 3:
    print "Uso correto: %s <servidor portal> <porta>" % str(sys.argv[0])

""" Port of the server """
port = int(sys.argv[2])
""" Server's name """
server = sys.argv[1]
""" Get IP server """
ip = socket.gethostbyname(server)
print "estabelecer conexão"
""" Establish connection """
try:
    s.connect((ip, port))
    ClientLog.logMessage( host + ": estabeleceu conexão: servidor portal: " + sys.argv[1])
except socket.error, ( errno, errmsg ):
    s.close()
    ClientLog.logMessage( "Erro ao realizar o connect(): " + str( errno ) + ": " + str( errmsg ) )
    sys.exit( 1 )       
    
print
choice = raw_input("Escolha o número do método que enviará o seu programa para um dos servidores: 1.Aleatório 2.Round-Robin ")
print
nome = raw_input("Escreva o nome do programa: ")
print

""" Open user's file """
filep = FileHandler()
filep.open(nome, 'r')
""" Keep file's data in 'dados' variable """
dados = filep.read()
filep.close()

""" Built a package """
package = Package(choice, nome, host, server, dados)

""" Transfer from package to string for transmission """
string = Convert.PackageToString(package)

""" Check if the transmition was possible """
try:
    Transmition.Send(s, string)
    ClientLog.logMessage( host + ": enviado arquivo fonte (" + nome + ") ao servidor portal: " + server)
except socket.error, ( errno, errmsg ):
    s.close()
    ClientLog.logMessage( "Erro ao enviar a mensagem: " + str( errno ) + ": " + str( errmsg ) )
    sys.exit( 1 ) 
    
ClientLog.logMessage(host + ": ---------------------------------------------------------------------")
ClientLog.logMessage(host + ": | esperando servidor portal: " + server + " retornar com a resposta |")
ClientLog.logMessage(host + ": ---------------------------------------------------------------------")

""" Check if client received the return message """
try:
    string = Transmition.Recv(s)
except socket.error, ( errno, errmsg ):
    s.close()
    ClientLog.logMessage( "Erro ao receber resultado da execução: " + str( errno ) + ": " + str( errmsg ) )
    sys.exit( 1 ) 
    
package = Convert.StringToPackage(string)

ClientLog.logMessage( host + ": recebimento do resultado da execução realizada no servidor de processamento: " + package.getNomeServer())

print package.getDados() 

""" Close the socket when done """
try:
    s.close()
    ClientLog.logMessage( host + ": encerramento da conexão")
except socket.error, ( errno, errmsg ):
    s.close()
    ClientLog.logMessage( "Erro ao encerrar conexão: " + str( errno ) + ": " + str( errmsg ) )
    sys.exit( 1 )
ClientLog.logMessage("-------------------------------------------------------------------------------------------------------------")
