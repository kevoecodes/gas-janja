from pymongo import MongoClient

from Mongo_DB.MongoDB import MongoDB
class OnlineUpdate(MongoDB):
    def __init__(self, status, deviceNo):
        super().__init__()
        self.status = status
        self.deviceNo = deviceNo
        self.update()

    def update(self):
        deviceInfo = self.devices_coll.find_one({"deviceNo": self.deviceNo})
        self.users_coll.update_one({"mobileNo": deviceInfo['mobileNo']}, {"$set": {"online_status": self.status}}, upsert=True)

class CheckOnlineStatus(MongoDB):
    def __init__(self, *args, **kwargs):
        super().__init__()
        print(kwargs)
        #self.deviceNo = kwargs['']
        for k, v in kwargs.items():
            if k == 'deviceNo':
                self.deviceNo = kwargs['deviceNo']
                self.num = False

            if k == 'mobileNo':
                self.mobileNo = kwargs['mobileNo']
                self.num = True
        
        self.check()


    def check(self):
        if self.num == True:
            self.userInfo = self.users_coll.find_one({"mobileNo": self.mobileNo})
            return
        else:

            deviceInfo = self.devices_coll.find_one({"deviceNo": self.deviceNo})
            self.userInfo = self.users_coll.find_one({"mobileNo": deviceInfo['mobileNo']})

    def feedback(self):
        #print(self.mobileNo)
        if self.userInfo['online_status'] == True:
            return  True
        return False



class AddToNotificationsQue:
    pass