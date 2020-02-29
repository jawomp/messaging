import socket
import sys
from tkinter import *

screen = Tk()
screen.title("anonify.it client")
screen.geometry("900x600")
screen.configure(background='#2e2e2e')
lbl = Label(screen, text="Running client")
lbl.grid(column=5, row=5)
screen.mainloop()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
print("host machine is: " + host)
lbl = Label(screen, text ="host machine is: " + host)
print("-----------------------------------")
address = ((host, port))
s.connect(address)
message = input('enter message: ')
lbl = Label(screen, text ="Input your message into the interpreter: ")
message = message.encode(encoding='UTF-8')
s.sendall(message)
data = s.recv(1024)
print(data)
s.close()