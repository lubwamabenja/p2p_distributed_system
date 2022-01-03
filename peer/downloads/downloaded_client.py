import socket

c = socket.socket() #creating a socket
c.connect(('localhost',9999)) #connect to the server socket

name = eval(input("Enter Your name: "))
c.send(bytes(name,'utf-8'))

print((c.recv(1024).decode()))