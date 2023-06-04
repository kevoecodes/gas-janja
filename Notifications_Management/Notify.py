from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime

from Mongo_DB.MongoDB import MongoDB

class Notify(MongoDB):
    def __init__(self, mobileNo, title, detail):
        super().__init__()
        self.mobileNo, self.title, self.detail = mobileNo, title, detail
        
        self.structureNotif()
        self.addNotification()

    def structureNotif(self):
        self.notification = {
            "_id": ObjectId(oid=None),
            "time": datetime.now(),
            "title": self.title,
            "body": self.detail
        }
    def addNotification(self):
        self.notifications_coll.insert_one(self.notification)








