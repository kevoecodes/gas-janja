from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .MongoCRUD import CheckOnlineStatus
from bson import json_util
import json


class PostToUserChannel:
    def __init__(self, deviceNo, data):
        print(data)
        self.channel_name, self.data = f"thread_{deviceNo}", data
        print(self.channel_name)
        online = CheckOnlineStatus(deviceNo = deviceNo)
        print(f'User is online: {online.feedback()}')
        if online.feedback() == True:
            #pass
            self.post_to_channel()
        

    def post_to_channel(self):
        layer = get_channel_layer()
        async_to_sync(layer.group_send)(self.channel_name, {
            "type": "send.message",
            "data": json.loads(json_util.dumps(self.data))
        })