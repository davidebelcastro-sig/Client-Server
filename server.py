import socket


HOST='localhost'
PORT=5000
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
