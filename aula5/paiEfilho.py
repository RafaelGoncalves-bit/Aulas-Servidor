import socket, os, time
from threading import Thread

HOST = 'localhost'
PORT = 65432

# Processo filho
def filho():
    global PORT
    PORT = PORT+1 #Porta+1
    f_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print('Filho ouvindo em',PORT) # Ouve na porta
    f_server.bind((HOST, PORT))
    f_server.listen()
    f_conn, f_addr = f_server.accept()
    with f_conn: # Ao aceitar nova conexão faz echo até letra q
        print ('Filho recebi uma conexão:', f_addr)
        while True:
            data=f_conn.recv(1024)
            if data:
                print('Filho recebi(',PORT,'):',data)
            if data == b'q':
                break
            f_connsendall(data)
# Processo pai
while True:
    p_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    p_server.bind((HOST, 65432))
    p_server.listen()
    print('Pai ouvindo em', 65432)
    p_conn, p_addr = p_server.accept()
    with p_conn: # Recebendo nova conexão
        print('Pai recebi uma conexão:', p_addr)
        p_conn.sendall(str.encode(str(PORT+1)))
        t=Thread(target=filho,args=()) # Cria processo filho
        t.start() # Inicia processo filho
p_server.close() # Força fechar conexão
