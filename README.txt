
Client.py

Ao iniciar o cliente é necessário passar por parâmetro o nome e a porta para comunicação com o servidor portal:
Ex.: python Client.py mumm 1234 -----> sendo "mumm" destinado para rodar o servidor portal
O cliente entao cria um socket para a comunicação. Se conecta com o servidor portal a partir da função connect() que recebe como parâmetro o IP do servidor e a porta que será utilizada, ex.: connect(("IP server", "port server")).
Realizada a conexão, é pedido ao cliente que digite a opção de escalonamento (aleatório ou Round-Robin) que o servidor portal deverá utilizar para escolher o servidor de processamento e logo após deve digitar o nome do arquivo fonte que deverá ser compilado e executado no servidor de processamento.
Em seguida o arquivo fonte é aberto para leitura, atribuindo o conteudo deste arquivo a uma variavel que será transmitida na area de dados do pacote.
Antes de transmitir, o pacote é convertido para uma string, para então poder ser transmitido.
Após a tansmissão, o cliente espera pelo retorno do resultado e quando recebê-lo, fechará o socket, finalizando a conexão.

PortalServer.py

Ao iniciar o servidor portal é necessário passar por parâmetro a porta a qual o servidor irá utilizar e todos os servidores de processamento que serão iniciados com suas respectivas portas.
Ex.: python PortalServer.py 1234 (serv. process.1) (porta1) (serv. process.2) (porta2) ... (serv. process.N) (portaN)
O servidor irá criar um socket para escutar, e precisará realizar um bind() desse socket para o seu endereço e a porta que esta utilizando.
O servidor irá realizar a função listen() apenas uma vez, antes de entrar em um laço, para saber quando uma conexão deve ser estabelecida. Ao detectar uma requisição de conexão, o servidor utiliza a função accept() para estabelecer uma conexão com o cliente. Feita essa conexão o servidor recebe do cliente um pacote contendo o arquivo fonte, a escolha do escalonamento (aleatório ou Round-Robin), o nome da maquina do cliente e o nome do arquivo fonte.
Foram criadas duas funções nesse servidor:

1ª - schedulingChoice():

-tem por objetivo receber o número da escolha (do cliente) de qual escalonamento usar;
-se a escolha for 1, é utilizada uma função random do python para retornar um numero aleatório no intervalo de [1 .. N] sendo N o numero de servidores de processamento;
-se a escolha for 2, é devolvida a variável numberServer que funciona como um contador, sempre seguindo uma ordem [1, 2, .., N] para enviar os pacotes para os servidores de processamento;
-o inteiro retornado por essa função é utilizado para escolher o servidor (argv[i]) e a porta correta no (argv[i+1]).

2ª - serverConnection(host, string, server, port):

-tem por objetivo criar um novo socket e estabelecer uma nova conexão com um dos servidores de precessamento para reenviar o pacote do cliente;
-é recebido como parametro: "host", "string" (que é o pacote a ser transmitido), "server" (que é o nome do servidor de processamento com o qual deve-se realizar conexão) e "port" (a porta a qual o servidor de precessamento esta atendendo).

Então, feito todos os procedimentos anteriores, o servidor portal irá enviar o pacote do cliente para um dos servidores de processamento e esperará pelo pacote de retorno do servidor de processamento para enviar ao cliente a resposta.

ProcessServer.py

O servidor de processamento irá criar um socket através do socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0), realizará o bind desse socket com o seu endereço e a porta que esta utilizando e logo em seguida realiza o listen() para ficar apto a "ouvir" por requisições.
O servidor entra em um laço para conseguir atender as requisições e sempre que chega uma requisição, é realizado o accept() para estabelecer uma conexão com o servidor portal.
Estabelecida a conexão e recebido o pacote proveniente do cliente, o servidor de processamento cria um arquivo localmente que irá receber o campo de dados do pacote e irá ser nomeado com o campo de "nome" do pacote, dessa forma é criado um arquivo fonte identico ao enviado pelo cliente e apto para ser compilado e executado.
Após a compilação e a execução, o resultado ou o erro é retornado ao cliente em um novo pacote criado pelo servidor.
Para conseguir retornar exatamente a saida da execução ou o erro da compilação foi utilizado o "subprocess.Popen", dessa forma, além da saída e do erro, é retornado também, através da função "process.returncode", um código de 0 ou 1. Quando é compilado sem erro e a saída da execução retornada, o process.returncode retorna 0, caso contrário retorna 1. A partir desse código é possível diferenciar quando deve-se retornar a saída de execução ou o erro de compilação.

FileHandler.py

Nesse arquivo foi criado uma classe na qual foram postas as principais funções para abrir, ler, escrever e fechar um arquivo.
Utilizado no cliente para ler o conteudo do arquivo fonte e também utilizado no servidor de processamento para criar um arquivo localmente (com o mesmo nome e conteúdo do arquivo fonte do cliente) para compilá-lo e executá-lo.

Package.py

Criada uma classe Pacote() que contem alguns campos para armazenar informações e dados. Muito utilizado no cliente e nos servidores para poder enviar todas as informações e dados, de uma só vez, ao destino.

Convert.py

Criada uma classe Protocolo() com funções que transformam do formato pacote para string (utilizado antes de uma transmissão) e do formato string para pacote (utilizado antes de mecher com os dados do pacote).

Transmition.py

Foi criado um protocolo de transmissão em que sempre que é enviado um pacote, logo em seguida é enviado um caracter de final de transmissão. Dessa forma, ao receber esse pacote, a função Recv() irá ficar recebendo todos os dados do pacote até encontrar um caracter de final de transmissão. Quando for encontrado esse caracter, é retirado o mesmo da string que acabou de ser recebida e retornada somente a string com os dados do pacote.

Log.py

Criada uma classe com uma função que recebe como parâmetro uma mensagem do acontecimento da execução do cliente ou dos servidores e essa mensagem é escrita em um arquivo, juntamente com a hora em que o acontecimento ocorreu.
