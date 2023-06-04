from pymongo import MongoClient

class MongoGet:
    def __init__(self, mobileNo):
        self.mobileNo = mobileNo
        print(self.mobileNo)
        self.conn()
        self.gotnotifs = self.getNotifs()

    def conn(self):
        self.client = MongoClient('mongodb://127.0.0.1:27017/')
        self.coll = self.client['GJJ']['notifications']

    def getNotifs(self):
        self.notifs = self.coll.find_one({"mobileNo": self.mobileNo})
        if self.notifs == None:
            return False
        
        return True
        

    def feedback(self):
        if self.gotnotifs:
            notif = self.notifs['notifications']
            return notif

        return {
            "notifications": False
        }