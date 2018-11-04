import socket

s=socket.socket()

host = "localhost"
port = 1236

s.connect((host, port))

s.send("abc")
s.close()