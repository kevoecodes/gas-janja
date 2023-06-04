
from pymongo import MongoClient


        
class MongoUpdateStatus:
    def __init__(self, data):
        self.deviceNo = data['deviceNo']
        self.data = data['status']

    def conn(self):
        self.client = MongoClient('mongodb://127.0.0.1:27017/')
        self.coll = self.client['GJJ']['devices']

    def update(self):
        self.coll.update_one({"deviceNo": self.deviceNo}, {"$set": {"user_portal": self.data}}, upsert=True)

    def feedback(self):
        pass