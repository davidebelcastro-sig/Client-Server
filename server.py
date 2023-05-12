import socket


fp = open("configurazione.txt", "r")
for riga in fp:
    valori = riga.split("=")
    if valori[0] == "HOST":
        HOST = valori[1]
        if HOST[-1] == "\n":
            HOST = str(HOST[:-1])
            
    elif valori[0] == "PORT":
        PORT = valori[1]
        if PORT[-1] == "\n":
            PORT = PORT[:-1]
        PORT = int(PORT)
fp.close()

# Crea un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associa il socket all'indirizzo e alla porta desiderati
server_address = (HOST, PORT)
sock.bind(server_address)

# Inizia ad ascoltare le connessioni in ingresso
sock.listen(1)
accettato = 0
# Accetta una nuova connessione
print('In attesa di una connessione...')
connection, client_address = sock.accept()
message = input("Accettare connessione con  "+ client_address[0]+"? ")
if message == 'no':
    print("Connessione rifiutata")
    connection.sendall(message.encode())
    connection.close()
    exit()
else:
    message = b'si'
    connection.sendall(message)
    print('Connessione accettata da', client_address)
    accettato = 1

if accettato == 1:
        while 1:

            #invio i comandi al client
            message = input("Inserisci un comando da inviare al client(exit per chiudere): ")
            connection.sendall(message.encode())
            if message == 'exit':
                connection.close()
                exit()
             # Riceve i dati dal client
            data = connection.recv(1024)
            print(client_address[0]+ ' ha inviato:', data.decode())