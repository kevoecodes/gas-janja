from Notifications_Management.Notify import Notify
from Mongo_DB.MongoDB import MongoDB
from Notifications_Management.Notify import Notify

class MongoSubscribe(MongoDB):
    def __init__(self, data):
        super().__init__()
        print(data)
        self.deviceNo = data['deviceNo']
        self.mobileNo = data['mobileNo']
        self.sub = int(data['subscription'])
        self.isfetched = self.Fetch()
        if self.isfetched and self.content:
            self.issubscribed = self.subscribe()

    def Fetch(self):
        try:
            self.deviceInfo = self.devices_coll.find_one({"deviceNo": self.deviceNo})
            self.user = self.users_coll.find_one({"mobileNo": self.mobileNo})
            if self.deviceInfo is not None and self.user is not None:
                self.content = True
                return True
            self.content = False
            return True
        except:
            return False

    def subscribe(self):
    
        self.devices_coll.update_one({"deviceNo": self.deviceNo}, {"$set": {"subscription": True}}, upsert=True)
        return True

    def notify(self):
        title = "Subscription"
        detail = f'Device {self.deviceNo} is subscribed to a monthly package'
        Notify(self.mobileNo, title, detail)

    def feedback(self):
        if self.isfetched and self.content and self.issubscribed:
            return  True
        return False
            
    