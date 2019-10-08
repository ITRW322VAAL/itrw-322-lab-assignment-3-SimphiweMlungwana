import socket

HOST = '127.0.0.1' #Server's IP address
PORT = 9999 # Server PORT number

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.sendall(b'Hello, Server')
    data = s.recv(1024)

    print('Received', repr(data))