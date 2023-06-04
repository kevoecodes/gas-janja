from django.shortcuts import render
from bson import json_util, ObjectId
import json
from rest_framework.response import Response
from rest_framework.views import APIView

""" from .MongoQuery import MongoCreate, MongoAddDevice

# Create your views here.
class Register_Account(APIView):
    def post(self, request, *args, **kwargs):
        mobileNo = request.data
        #print(post)
        create = MongoCreate(mobileNo)
        feed = create.feedback()
        print(feed)
        return Response(json.loads(json_util.dumps(feed)))

class Add_Device(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        #print(post)
        create = MongoAddDevice(data)
        feed = create.feedback()
        #print(feed)
        return Response(json.loads(json_util.dumps(feed)))
 """