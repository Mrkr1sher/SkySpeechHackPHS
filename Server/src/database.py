from pymongo import MongoClient

db = MongoClient()['skyspeech']
messages = db.messages