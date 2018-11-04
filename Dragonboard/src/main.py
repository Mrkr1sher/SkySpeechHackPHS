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

              

    inData = None

    while True:

        s.listen(5)     

        c, addr = s.accept() 

        while True:
            print("accepted connection")    
        
            inData = c.recv(1024)

            print("Data" + str(inData))

            dumpData(inData)


print("Listen for updates ")
listenForUpdates()
    

