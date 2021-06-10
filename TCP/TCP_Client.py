# Feito por Arthur Eduardo Good
# Redes I - 2021/01

import socket

HOST = ''  # IP do host(servidor)
PORT = 0        # A porta utilizada pelo servidor

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Laboratorio TCP')
    data = s.recv(1024)

print('Recebido', repr(data))