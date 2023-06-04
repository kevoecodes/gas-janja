from bson import json_util, ObjectId
import json
#from pymongo import response
from django.http import QueryDict

from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .MongoQuery import MongoFetch
from .MongoChange import MongoChange

class Get_Info(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        device = MongoFetch(data['deviceNo'][0]['desviceNo'])
        feed = device.feedback()
        return Response(json.loads(json_util.dumps(feed)))

class Change_Info(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        device = MongoChange(data)
        feed = device.feedback()
        
        return Response(json.loads(json_util.dumps(feed)))