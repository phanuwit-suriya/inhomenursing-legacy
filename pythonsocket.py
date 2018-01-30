import socket
import time

HOST = "127.0.0.1"
PORT = 8080

sock = socket.socket()
sock.connect((HOST, PORT))

hello = "Hello\n"
bye = "Bye\n"

sock.sendall(hello.encode())
data = sock.recv(1024)
print("1\) ", data)

if data:
    sock.sendall(bye.encode())
    data = sock.recv(1024)
    print("2) ", data)
    print(type(data))

    if data:
        sock.close()
        print("Socket closed")

