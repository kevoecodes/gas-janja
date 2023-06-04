from Notifications_Management.Notify import Notify
from pymongo import MongoClient

class MongoAddDevice:
    def __init__(self, data):
        print(data)
        self.deviceNo = data['deviceNo']
        self.mobileNo = data['mobileNo']
        self.query = {
            "mobileNo": self.mobileNo
        }
        self.data = data
        self.conn()
        self.userExists = self.checkExs()
        self.devNoExists = self.checkDevExc()
        if self.userExists:
            if not self.devNoExists:
                self.added = self.addDevice()
                if self.added:
                    print("Added--------")
                    re = self.notify() 

    def conn(self):
        self.client = MongoClient('mongodb://127.0.0.1:27017/')
        self.coll = self.client['GJJ']['Users']

    def checkExs(self):
        user = self.coll.find_one(self.query)
        if user == None:
            return False
        return True

    def checkDevExc(self):
        devNo = self.client['GJJ']['devices'].find_one({"deviceNo": self.deviceNo})
        if devNo == None:
            return False
        
        return True

    def addDevice(self):
        try:
            initial_data = {
                "mobileNo": self.mobileNo,
                "deviceNo": self.deviceNo,
                "isconnected": False,
                "isleaking": False,
                "conditon": None,
                "units": None,
                "cylinderUnits": None         
            }
            self.client['GJJ']['devices'].insert_one(initial_data)
            devices = []
            devs = self.client['GJJ']['devices'].find(self.query)
        
            for i in devs:
                print(i)
                cc = {}
                cc['_id'] = i['_id']
                cc['deviceNo'] = i['deviceNo']
                cc['subscription'] = 0
                print(cc)
                devices.append(cc)

            self.coll.update_one({"mobileNo": self.mobileNo}, {"$set": {"devices": devices}}, upsert=True)
            self.user = self.coll.find_one({"mobileNo": self.mobileNo})
            print({"User": self.user})
            return True
        except:
            self.resp = "Something went wrong"
            return False
        finally:
            print(f'Addition of new devices on {self.mobileNo}')

    def notify(self):
        title = "Device Added"
        detail = f'Device {self.deviceNo} was added to your account'
        Notify(self.mobileNo, title, detail)
        print("Went to addingg----")
        return True

    def feedback(self):
        if self.userExists and not self.devNoExists and self.added:
            feed = {
                "isadded": True,
                "addedDevice": self.data,
            }
            return feed
        elif self.devNoExists:
            feed = {
                "isadded": False,
                "detail": "Device already registered"
            }
            return feed
        
        elif not self.userExists:
            feed = {
                "isadded": False,
                "detail": "User not found"
            }
            return feed

        elif self.added:
            feed = {
                "isadded": False,
                "detail": self.resp
            }

            return feed

        return {"detail": "Something went horribly wrong"}