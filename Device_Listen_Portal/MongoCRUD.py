from pymongo import MongoClient
from Mongo_DB.MongoDB import MongoDB
from Notifications_Management.Notify import Notify
from Notifications_Management.PushNotifiication import PushNotification

class MongoUpdate(MongoDB):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.deviceNo = data['deviceNo']
        self.amnt = data['units']

        self.fetched = self.Fetch()
        if self.fetched and self.exists:
            self.isupdated = self.update()
            if float(self.amnt) == 75 or float(self.amnt) == 50 or float(self.amnt) == 25 and self.data['isconnected'] and not self.data['isleaking']:
                self.notify()
            if float(self.amnt) == 20 or float(self.amnt) == 15 or float(self.amnt) == 10 or 0 < float(self.amnt) < 6 and self.data['isconnected'] and not self.data['isleaking']:
                self.notifyDanger()
            if float(self.amnt) == 0 and self.data['isconnected']:
                self.notifyFinish()
            if not self.data['isconnected']:
                self.notifyDisc()

            if self.data['isconnected'] and self.data['isleaking']:
                self.notifyLeak()


    def Fetch(self):
        #print(self.mobileNo)
        try:
            self.deviceInfo = self.devices_coll.find_one({"deviceNo": self.deviceNo})
            if self.deviceInfo is not None:
                self.exists = True
            return True
        except:
            return False
        finally:
            pass

    def update(self):
        self.devices_coll.update_one({"deviceNo": self.deviceNo}, {"$set": {"units": self.data['units'], "isleaking": self.data['isleaking'], "isconnected": self.data['isconnected']}})
        return True

    def notify(self):
        title = "Device Update"
        detail = f'Device {self.deviceNo} has {self.amnt} units remaining'
        Notify(self.deviceInfo['mobileNo'], title, detail)
        
        if self.user_info['user_status'] == True:
            PushNotification()

        return True
    
    def notifyDanger(self):
        title = "Device Update"
        detail = f'Device {self.deviceNo} is about to finish, has {self.amnt} units remaining, Please refill.'
        Notify(self.deviceInfo['mobileNo'], title, detail)
        return True

    def notifyFinish(self):
        title = "Device Update"
        detail = f'Device {self.deviceNo} has finished, Please refill.'
        Notify(self.deviceInfo['mobileNo'], title, detail)
        return True

    def notifyDisc(self):
        title = "Device Disconnected"
        detail = f'Device {self.deviceNo} has being disconnected, or not properly connected, please check it.'
        Notify(self.deviceInfo['mobileNo'], title, detail)
        return True

    def notifyLeak(self):
        title = "Cylinder Leakage"
        detail = f'Cylinder with device {self.deviceNo} is leaking, please attend to it urgently.'
        Notify(self.deviceInfo['mobileNo'], title, detail)
        return True

    def feedback(self):
        if self.fetched and self.isupdated and self.exists:
            return self.deviceInfo['subscription']

        return False

           
        