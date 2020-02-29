# when testing, ensure you run server and client in separate interpreters
# also ensure server runs before client
#to do:
#decode server packet from utf-8 to ascii

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
print("host machine is: " + host)
print("-----------------------------------")
address = ((host, port))
s.connect(address)
message = input('enter message: ')
message = message.encode(encoding='UTF-8')
s.sendall(message)
data = s.recv(1024)
print(data)
s.close()
