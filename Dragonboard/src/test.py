import socket

s=socket.socket()

host = "172.16.243.226"
port = 1234

s.connect((host, port))

s.send("asdadas")
s.close()