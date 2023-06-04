from django.shortcuts import render
from rest_framework.views import APIView
from bson import json_util, ObjectId
import json
from .MongoCRUD import MongoGet
from django.http import QueryDict

from rest_framework.response import Response

# Create your views here.
class GetUserNotifs(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data

        print(data)
        notifs = MongoGet(data['mobileNo'])
        feed = notifs.feedback()
        return Response(json.loads(json_util.dumps(feed)))