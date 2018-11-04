import requests
import json


link = ""
key = "Chris"

messageList =  json.load(open("messages.json"))

def uploadAllTheMessages():

    for i in messageList:

        uploadMessage(i["message"])


def uploadMessage(message):

    payload = {"key" : key : "message" : message}

    r = requests.post(link, data=payload)

