import requests
import json


link = "http://18.216.42.131/api/postmessage"
key = "Chris"

messageList =  json.load(open("messages.json"))

def uploadAllTheMessages():

    for i in messageList:

        uploadMessage(i)


def uploadMessage(message):
    print(message)

    r = requests.post(link, data=message)

uploadAllTheMessages()