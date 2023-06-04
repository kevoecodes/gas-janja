from datetime import datetime
from bson import json_util, ObjectId
from pymongo import MongoClient
import json
from channels import layers
from channels.auth import _get_user_session_key
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from Channels_Manager.User_channel import PostToUserChannel

#from pymongo import response
from django.http import QueryDict
from .MongoCRUD import MongoUpdate
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


class Device_Portal(APIView):
    def post(self, request, *args, **kwargs):
        #data = {}
        data = request.data
        print(type(data))
        if type(data) == QueryDict:
            data = dict(request.data.dict())
            print(type(data))
    
        print(data)
        if data["isleaking"] == "1":
            data['isleaking'] = True

        if data["isleaking"] == "0":
            data['isleaking'] = False

        if data["isconnected"] == "1":
            data['isconnected'] = True

        if data["isconnected"] == "0":
            data['isconnected'] = False

        print(data)
        update = MongoUpdate(data)
        feed = update.feedback()
        PostToUserChannel(data['deviceNo'], data)
        return Response(feed)

