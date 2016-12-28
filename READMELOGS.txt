
-- Especificação dos logs --

Para a execução usamos cinco hosts diferentes do DINF: caporal, mumm, dalmore, priorat e bowmore; onde executamos três servidores, um cliente e um portal para o desenvolvimento da "Nano-Nuvem". Segue a relação com função, host, porta e log de retorno:

FUNÇÃO 	    HOST 	    PORTA 	LOG DE RETORNO
Servidor 	dalmore 	1234 	ProcessServerLog_dalmore.txt
Servidor 	priorat 	1235 	ProcessServerLog_priorat.txt
Servidor 	bowmore 	1236 	ProcessServerLog_bowmore.txt
Cliente 	caporal 	2345 	ClientLog_caporal.txt
Portal 	    mumm 	    2345 	PortalServerLog_mumm.txt

As linhas de execução respectivas à tabela, nos host especificados, foram:
>> python ProcessServer.py 1234
>> python ProcessServer.py 1236
>> python ProcessServer.py 1235
>> python Client.py mumm 2345
>> python PortalServer.py 2345 dalmore 1234 priorat 1235 bowmore 1236

No total, dezoito solicitações de execuçãoo foram feitas pelo cliente, sendo nove usando o modo aleatório e as outras nove usando o método Round-Robin, isto está sinalizado no log "PortalServerLog_mumm.txt". Além disto, quatro arquivos em python foram chamadas pelo cliente à execução, sendo eles: "fibonacci.py", "numerosPerfeitos.py", "teste.py" e "lista.py".
