import requests
import json


link = "127.0.0.1:5000/postmessage"
key = "Chris"

messageList =  json.load(open("messages.json"))

def uploadAllTheMessages():

    for i in messageList:

        uploadMessage(i)


def uploadMessage(message):

    payload = {"data" : message}

    print(payload)

    #r = requests.post(link, data=payload)

uploadAllTheMessages()