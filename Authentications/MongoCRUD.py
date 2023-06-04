from datetime import datetime
from Mongo_DB.MongoDB import MongoDB


class MongoCreate(MongoDB):
    def __init__(self):
        super().__init__()

    def CreateAcc(self, data):
        try:
            user = {}
            user['mobileNo'] = data['mobileNo']
            user['created_at'] = datetime.now()
            user['online_status'] = False
            #user['']
            self.users_coll.insert_one(user)
            return True
        except:
            return False
        finally:
            print("Creation of a new account")

  
class MongoUsers(MongoDB):
    def __init__(self):
        super().__init__()

    def isUser(self, data):
        user = self.users_coll.find_one({"mobileNo": data})
        print('user', user)
        if user is None:
            return False

        return True



class MongoFetch(MongoDB):
    def __init__(self, mobileNo):
        super().__init__()
        self.mobileNo = mobileNo
        self.fetched = self.Fetch()

    def Fetch(self):
        #print(self.mobileNo)
        try:
            self.user = self.users_coll.find_one({"mobileNo": self.mobileNo})
            return True
        except:
            return False
        finally:
            #Writting loggs
            print("Fetching data")

    def feedback(self):
        if self.fetched:
            feed = {
                "islogin": True,
                "token": "wef-fwef-we-sf-wefwsefwefs-fd",
                "user": self.user
            }
            return feed

        return {
            "isfetched": False,
            "detail": "Something went wsrong"
        }
        