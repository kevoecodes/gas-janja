from django.shortcuts import render
from bson import json_util, ObjectId
import json
from rest_framework.response import Response
from rest_framework.views import APIView

from .MongoCRUD import MongoSubscribe

#from .MongoQuery import MongoCreate, MongoAddDevice

# Create your views here.
class Subscribe_Device(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        update = MongoSubscribe(data)
        feed = update.feedback()  
        return Response(json.loads(json_util.dumps(feed)))