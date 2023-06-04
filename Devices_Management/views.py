from datetime import datetime
from bson import json_util, ObjectId
from pymongo import MongoClient
import json

from Channels_Manager.User_channel import PostToUserChannel

#from pymongo import response
from django.http import QueryDict
from .MongoCRUD import MongoDevicesManagement, MongoAddDevice
from rest_framework.response import Response
from rest_framework.views import APIView
#from User_Listen_Portal.consumer import User_Dev_Portal

class TestDevice(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        print(type(data))
        if type(data) == QueryDict:
            data = dict(request.data.dict())
            
        print(data)
    
        data['at'] = datetime.now()
        client = MongoClient('mongodb://127.0.0.1:27017/')
        coll = client['GJJ']['data_type_sent']
        coll.insert_one(data)

        return Response(False)

class GetUserDevice(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        device = MongoDevicesManagement().getUserDevice(data)

        return Response(json.loads(json_util.dumps(device)))

class GetUsersDevices(APIView):
    def post(self, request, *args, **kwargs):
        #data = {}
        data = request.data
        print(type(data))
        
        devices = MongoDevicesManagement().getUserDevices(data)
        print(devices)
        
        return Response(devices)


class Add_Device(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        #print(post)
        create = MongoAddDevice(data)
        feed = create.feedback()
        #print(feed)
        return Response(json.loads(json_util.dumps(feed)))

