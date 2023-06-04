from bson import json_util, ObjectId
import json
#from pymongo import response
#from django.http import QueryDict
#from .MongoCRUD import MongoFetch
from Devices_Management.MongoCRUD import MongoDevicesManagement
from rest_framework.response import Response
from rest_framework.views import APIView

class User_Portal(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        update = MongoDevicesManagement().getUserDevice(data)
        
        
        return Response(json.loads(json_util.dumps(update)))