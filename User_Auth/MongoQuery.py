from re import escape
from pymongo import MongoClient, response

class MongoUsersExists:
    def __init__(self, mobileNo):
        self.mobileNo = mobileNo
        self.conn()
        self.userExists = self.checkExs()

    def conn(self):
        self.client = MongoClient('mongodb://127.0.0.1:27017/')
        self.coll = self.client['GJJ']['Users']

    def checkExs(self):
        #print(self.mobileNo)
        user = self.coll.find_one({"mobileNo": self.mobileNo})
        #print(user)
        if user == None:
            return False
        return True

    def feedback(self):
        if self.userExists:
            return True
                
        return False

class MongoFetch:
    def __init__(self, mobileNo):
        self.mobileNo = mobileNo
        self.conn()
        self.fetched = self.Fetch()

    def conn(self):
        self.client = MongoClient('mongodb://127.0.0.1:27017/')
        self.coll = self.client['GJJ']['Users']

    def Fetch(self):
        #print(self.mobileNo)
        try:
            self.user = self.coll.find_one({"mobileNo": self.mobileNo})
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
        