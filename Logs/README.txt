        
                                           --   Especifica��o dos logs --

  Para a execu��o usamos tr�s hosts diferentes do DINF: ploc, dorno e bart; onde executamos tr�s servidores, um cliente e um portal para o desenvolvimento da "Nano-Nuvem". Segue a rela��o com fun��o, host, porta e log de retorno:


                               
                                ---------------------------------------------------------                                                 
                               |FUN��O      | HOST  | PORTA | LOG DE RETORNO             |
                               -----------------------------------------------------------
                               |Servidor    |bart   |1234   | ProcessServerLog_bart.txt  |
                               |Servidor    |dorno  |1236   | ProcessServerLog_dorno.txt |
                               |Servidor    |ploc   |1235   | ProcessServerLog_ploc.txt  |
                               |Cliente     |dorno  |2345   | ClientLog_dorno.txt        |
                               |Portal      |bart   |2345   | PortalServerLog_bart.txt   |
                                ---------------------------------------------------------

 As linhas de execu��o respectivas � tabela, nos host especificados, foram:
 >> python ProcessServer.py 1234
 >> python ProcessServer.py 1236
 >> python ProcessServer.py 1235
 >> python Client.py 2345 bart
 >> python PortalServer.py 2345 bart 1234 dorno 1236 ploc 1235



 No total, dezoito solicita��es de execu��o foram feitas pelo cliente, sendo doze usando o modo aleat�rio e as outras seis usando o m�todo Round-Robin, isto est� sinalizado no log "PortalServerLog_bart.txt". Al�m disto, quatro arquivos em python foram chamadas pelo cliente � execu��o, sendo eles: "fibonacci.py", "numerosPerfeitos.py", "teste.py" e "lista.py".
