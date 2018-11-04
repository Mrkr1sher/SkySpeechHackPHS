import requests
import json


link = "http://172.16.240.43:80/api/postmessage"
key = "Chris"

messageList =  json.load(open("messages.json"))

def uploadAllTheMessages():

    for i in messageList:

        uploadMessage(i)


def uploadMessage(message):
    print(message)

    r = requests.post(link, data=message)

uploadAllTheMessages()