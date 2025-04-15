import socket

# Definições de host e porta
HOST = 'localhost'
PORT = 65432
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print('Pedi conexão na porta:', PORT)
    porta = s.recv(1024)
    print('O servidor quer me anteder em:',repr(porta))
    s.close()
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.connect((HOST,int(porta)))
        print('Fui para a aconexão na porta:',porta)
        while True:
            texto = input('Digite alguma coisa para enviar ou q para sair:')
            s.sendall(str.encode(texto))
            data = s.recv(1024)
            print('Recebi de volta:', repr(data))
            if texto == 'q':
                break
