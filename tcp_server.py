import socket # import networking
import sys # import sys in case networking requires it

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # build socket 's' as tcp
print('socket created') # debugging
host = socket.gethostname() # get host name of local machine
port = 12345 # random port number, non privileged (>1000s)
s.bind((host, port)) # bind to hostname and port as tuple (2 brackets)
s.listen(5) # start tcp listener, wait for 5 connections
print('waiting for con') # debugging
connection, client = s.accept() # accept connection from client
print('connected') # debugging
data = connection.recv(16) # accept 16 byte packets (?) (need more info on recv function)
print('received "%s"' % data) # debugging
connection.sendall(data) # send back received packet
