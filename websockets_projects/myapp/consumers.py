import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import time, random

class MyConsumer(WebsocketConsumer):
    def connect(self):
        print("WebSocket connected")
        self.accept()
        self.send(text_data=json.dumps({
            "message": f"✅ WebSocket connection established. Waiting for updates..."
        }))
        self.handle()

    def disconnect(self, close_code):
        async_to_sync(get_channel_layer().group_discard)(
            self.group_name,
            self.channel_name
        )
        print("WebSocket disconnected")

    def receive(self, text_data):
        """If client sends data back, just log it."""
        print("Received from client:", text_data)

    def handle(self):
        count = 0
        data = [0,0,0,0]
        while True:
            a1 = random.randint(10, 100)
            a2 = random.randint(10, 100)
            a3 = random.randint(10, 100)
            a4 = random.randint(10, 100)
            data = [a1, a2, a3, a4]
            time.sleep(5)
            count += 1
            if count > 10:
                break
            # self.send(text_data=json.dumps({
            #     "message": f"send_update{count}"
            # }))
            self.send(text_data=json.dumps({
                "label": f"Update {count}",
                "value": data
            }))

