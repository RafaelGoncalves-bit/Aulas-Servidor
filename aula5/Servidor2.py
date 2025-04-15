import socket

HOST = 'localhost'
PORT = 65432

cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cliente.connect((HOST,PORT))
cliente.sendall(b'Ei, estou aqui!')
data = cliente.recv(1024)

print('Recebi de volta:',repr(data))
