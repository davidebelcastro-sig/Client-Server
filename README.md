# Client-Server
A program that connects server and client (on two different machines) and the server sends commands for the client to execute on the other machine, the client sends the output to it. The client is written and executed by a graphical interface which implements a calculator.

When the user decides to calculate the result of an operation on the calculator, the client is created and executed, if the server is already active in the other machine, a client-server connection is established and the server can send commands to be executed by the clients.
The client remains active until the server closes the connection. The user can continue to use the calculator or close it, the client will still remain active in background.

# To Run

Insert in configurazione.txt HOST(IP) of the server
Insert IP of the server in the file server.py
Run server.py on a computer,and calcolatrice.py in other machine.
When the user click "=" on the calculator,start the connection with server and client
The file configurazione.txt must be present in machine where is the client.py/calcolatrice.py.


# WARNING

The program was written for a client server exercise in python. NOT TO BE USED FOR ILLEGAL PURPOSES.
I DO NOT ASSUME ANY RESPONSIBILITY FOR IMPROPER USE OF THE PROGRAM!!!.
