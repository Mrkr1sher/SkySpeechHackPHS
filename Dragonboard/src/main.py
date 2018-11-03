import socket
import json

port = 1234
localIp  = "172.16.243.226"

#Dump function
def dumpData(data):

    f = open("messages.json")
    if f == None:
        f = open("messages.json", "w+")
        json.dump([], f)
        f.close()
        f = open("messages.json", "r")

    currentData = json.load(f)
    
    currentData.append()

    f.close()
    f = open("messages.json")
    json.dump(f, currentData)

    f.close()

    return

#Listen function
def listenForUpdates():
    s = socket.socket()
    s.bind((localIp, port))

    s.listen(5)               

    inData = None

    while True:
        c, addr = s.accept() 

        print("accepted connection")    
    
        inData = c.recv(1024)

        print(inData)

        if(inData[:3] == "MS:"):
          dumpData(inData)  

print("Listen for updates ")
listenForUpdates()
    

