from pymongo import MongoClient

class MongoChange:
    def __init__(self, device):
        self.deviceNo = device['deviceNo']
        self.amnt = device['amnt']
        self.conn()
        self.fetched = self.Fetch()
        if self.fetched:
            self.change()

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

    def change(self):
        self.coll.update_one({"deviceNo": self.deviceNo}, {"$set": {"availableLitres": self.amnt}}, upsert=True)


    def feedback(self):
        if self.fetched:
            feed = True
            return feed

        return {
            "isfetched": False,
            "detail": "Something went wrong"
        }
        