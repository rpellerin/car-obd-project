#!/usr/bin/env python

import asyncio
import websockets
import time
from random import randint
from threading import Thread

async def hello(websocket, path):
    print("connected")

    toSend = 0;
    while True:
        try:
            print("ready to send")
            await websocket.send(str(toSend))
            print("sent")
        except:
            print("breaking")
            break
        time.sleep(0.01)
        toSend = (toSend + 1) % 130
        if toSend == 0:
            toSend = 0

    #name = await websocket.recv()
    #print("< {}".format(name))

    #greeting = "Hello {}!".format(name)
    #await websocket.send(greeting)
    #print("> {}".format(greeting))


start_server = websockets.serve(hello, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
