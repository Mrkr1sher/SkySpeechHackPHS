import socket
import json

port = 1236
localIp  = "localhost"

#Dump function
def dumpData(data):

    data = data.decode("utf-8")


    data = json.loads(data)
    print(data)

    f = open("messages.json","r")

    currentData = json.load(f)
    
    currentData.append(data)

    f.close()

    print(currentData)

    f = open("messages.json","w")
    json.dump(currentData, f)

    f.close()

    return

#Listen function
def listenForUpdates():
    s = socket.socket()
    s.bind((localIp, port))

              

    inData = None

    while True:

        s.listen(-1)  

        conn, accept = s.accept()
        
        print("Device connected")
        while True:
            data = conn.recv(1024)
            if not data : break
            print("Data received : "  + str(data))
            dumpData(data)
            conn.send(bytes("server confirming", "utf-8"))

            

print("Listen for updates ")
listenForUpdates()
    

