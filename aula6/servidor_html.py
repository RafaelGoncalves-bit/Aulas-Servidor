import socket

HOST='localhost'
PORT=80


servidor=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Ouvindo em ',PORT)
servidor.bind((HOST,PORT))
servidor.listen()
conn,addr=servidor.accept()
with conn:
    print('Recebi uma conexão: ',addr)
    data=conn.recv(1024)
    print('Recebi ',data)
    resposta='HTTP/1.1 200 OK\n'
    resposta=resposta+'Content-Type:text/html\n'
    resposta=resposta+'\n'
    conn.sendall(str.encode(resposta))
    arq=open('hello_world.html','r')
    conn.sendall(str.encode(arq.read()))
    arq.close()
    
servidor.close()
