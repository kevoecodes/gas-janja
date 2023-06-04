import asyncio
import json
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
import datetime
class User_Notifications_Portal(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected", event)
        self.channel = f"thread_{self.scope['ref_url']}"
        await self.channel_layer.group_add(
            self.channel,
            self.channel_name
        )
        #print(self.scope)
        await self.send({
            "type": "websocket.accept"
        })
        #Check if there are user's unseen notifications
        #Then send them if there are.

    async def websocket_receive(self, event):
        print("Message: ", event['text'])

    async def send_message(self, event):
        print('messages', event)
        await self.send(
            {
                "type": "websocket.send",
                "content": event['content']
            }
        )

    async def websocket_disconnect(self, event):
        print("disonnected", event)
        await self.channel_layer.group_discard(
            "thread_1",
            self.channel_name
        )

    #@database_sync_to_async
    def receive_data(self, event):
        print('data', event)
        self.send({
            "type": "websocket.send",
            "text": "Hello world"
        })
        #await self.send(event)

class Do:
    def __init__(self, data):
        print({"consumer-data": data})
