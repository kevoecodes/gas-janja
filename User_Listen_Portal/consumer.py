from channels.exceptions import StopConsumer
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from Channels_Manager.MongoCRUD import OnlineUpdate
#from User_Listen_Portal.MongoCRUD import MongoFetch
from Devices_Management.MongoCRUD import MongoDevicesManagement
import json
from bson import json_util

class User_DevUpdates_Consumer(AsyncJsonWebsocketConsumer):
    async def websocket_connect(self, event):
        print("connected", event)
        print(self.scope['path_remaining'])
        self.deviceNo = self.scope['path_remaining']
        self.thread_name = f"thread_{self.deviceNo}"
        print(self.thread_name)
        await self.channel_layer.group_add(
            self.thread_name,
            self.channel_name
        )
        OnlineUpdate(True, self.deviceNo)
        print('ll')
        await self.accept()
        await self.fetch_device_data()
        await self.send_json(json.loads(json_util.dumps(self.device_data)))
        

    async def websocket_receive(self, event):
        print("Message: ", event['text'])

        await self.channel_layer.group_send(
            "thread_1",
            {
                "type": "send.message",
                "data": event['text']
            }
        )

    async def send_message(self, event):
        print('messages', event)
        
        await self.send_json(event['data'])


    async def websocket_disconnect(self, event):
        print("disonnected", event)
        OnlineUpdate(False, self.deviceNo)
        await self.channel_layer.group_discard(
            self.thread_name,
            self.channel_name
        )
        await self.disconnect(event['code'])
        raise StopConsumer()

    @database_sync_to_async
    def fetch_device_data(self):
        print(self.deviceNo)
        data = MongoDevicesManagement().getUserDevice({"deviceNo": self.deviceNo})
        print(data)
        self.device_data = json.loads(json_util.dumps(data))


