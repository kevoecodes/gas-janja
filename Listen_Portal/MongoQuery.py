
from pymongo import MongoClient

class MongoFetch:
    def __init__(self, deviceNo):
        self.deviceNo = deviceNo
        self.conn()
        self.fetched = self.Fetch()

    def conn(self):
        self.client = MongoClient('mongodb://127.0.0.1:27017/')
        self.coll = self.client['GJJ']['devices']

    def Fetch(self):
        #print(self.mobileNo)
        try:
            self.deviceInfo = self.coll.find_one({"deviceNo": self.deviceNo})
            return True
        except:
            return False
        finally:
            #Writting loggs
            print(f'Fetching device data for {self.deviceNo}')

    def feedback(self):
        if self.fetched:
            feed = self.deviceInfo
            return feed

        return {
            "isfetched": False,
            "detail": "Something went wrong"
        }
        