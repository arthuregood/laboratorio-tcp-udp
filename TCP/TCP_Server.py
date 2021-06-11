# Feito por Arthur Eduardo Good
# Redes I - 2021/01

import socket

HOST = '127.0.0.1'  # localhost padrão
PORT = 5005        # Porta a ser utilizada

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Conectado por', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)