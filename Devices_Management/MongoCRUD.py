from Mongo_DB.MongoDB import MongoDB
from Notifications_Management.Notify import Notify

class MongoDevicesManagement(MongoDB):
    def __init__(self):
        super().__init__()

    def getUserDevices(self, data):
        devices = self.devices_coll.find({"mobileNo": data['mobileNo']})
        devices_data = []
        for device in devices:
            device_data = {}
            device_data['subscription'] = device['subscription']
            device_data['device_name'] = "Gas_01"
            device_data['deviceNo'] = device['deviceNo']
            device_data['units'] = device['units']

            devices_data.append(device_data)

        return devices_data

    def getUserDevice(self, data):
        device = self.devices_coll.find_one({"deviceNo": data['deviceNo']})
        #del device['_id']
        return device



class MongoAddDevice(MongoDB):
    def __init__(self, data):
        super().__init__()
        print(data)
        self.deviceNo = data['deviceNo']
        self.mobileNo = data['mobileNo']
        self.query = {
            "mobileNo": self.mobileNo
        }
        self.data = data
     
        self.userExists = self.checkExs()
        self.devNoExists = self.checkDevExc()
        if self.userExists:
            if not self.devNoExists:
                self.added = self.addDevice()
                if self.added:
                    print("Added--------")
                    re = self.notify() 

    def checkExs(self):
        user = self.users_coll.find_one({"mobileNo": self.data['mobileNo']})
        if user == None:
            return False
        return True

    def checkDevExc(self):
        devNo = self.devices_coll.find_one({"deviceNo": self.deviceNo})
        if devNo == None:
            return False
        
        return True

    def addDevice(self):
        try:
            initial_data = {
                "subscription": False,
                "mobileNo": self.mobileNo,
                "deviceNo": self.deviceNo,
                "isconnected": False,
                "isleaking": False,
                "conditon": None,
                "units": None,
                "cylinderUnits": None         
            }
            self.devices_coll.insert_one(initial_data)
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


    

