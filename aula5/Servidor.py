import socket

#Definição de host e porta
HOST = 'localhost'
PORT = 65432
servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Ouvindo em ', PORT)
servidor.bind((HOST,PORT))
servidor.listen()
conn,addr = servidor.accept()
with conn:
    print('Recebi uma conexão:',addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print('Recebi:',data)
        conn.sendall(data)
