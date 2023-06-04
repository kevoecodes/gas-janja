
from bson import json_util, ObjectId
import json
#from pymongo import response
from django.http import QueryDict

from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .MongoCRUD import MongoUsers, MongoCreate, MongoFetch
from .serializers import LoginSerializer

class Login_User(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        userExst = MongoUsers().isUser(data['mobileNo'])
        if not userExst:
            print('stage1')
            feed = {
                "islogin": False,
                "detail": "Account unknown"
            }
            return Response(feed)
        print('stage-2')
        data_dict = QueryDict('', mutable=True)
        data_dict.update(data)
        serializer = LoginSerializer(data=data_dict)
        if serializer.is_valid():
            if userExst:
                user = MongoFetch(data['mobileNo'])
                feed = user.feedback()
                print(feed)
                return Response(json.loads(json_util.dumps(feed)))
            
            feed = {
                "islogin": False,
                "destail": "User account not found, regiser instead"
            }
            return Response(feed)

        return Response(serializer.errors)

class Register_User_Number(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        #print(post)
        userExst = MongoUsers(data['mobileNo']).isUser()
        if not userExst:
            feed = {
                "islogin": False,
                "detail": "Account unknown"
            }
            return Response(feed)
        #Check user in the Users model
        #Add the number to Users model
        #Generate unique code, and store in MongoDB, with a unique ID


class Verify_Code(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        #Check the code in the mongoDB, using the given unique ID


class CreatePass(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        #Create a password for the user in the Users model



class Register_Account(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
  
        if not MongoUsers().isUser(data['mobileNo']):
            create = MongoCreate().CreateAcc(data)

            return Response(create)

        return Response(False)
        #return Response(json.loads(json_util.dumps(data)))

