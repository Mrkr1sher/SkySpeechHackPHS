from pymongo import MongoClient

db = MongoClient()['skyspeech']
messagecollection = db.messages

def post_message(messagejson):
    if messagejson['key'] == "Chris":
        if messagejson['content'] == "" or messagejson['sender'] == "":
            return "Please fill out all fields"
        messagecollection.insert_one(messagejson)
        return "SUCCESS"
    return "STOP HAXING"