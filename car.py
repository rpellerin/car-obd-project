import obd
import signal
import sys
import asyncio
import websockets
import time
from random import randint
from threading import Thread

connection = obd.OBD("/dev/ttyUSB0")

async def hello(websocket, path):
    print("connected")

    cmd = obd.commands.SPEED

    while True:
        r = connection.query(cmd)
        try:
            print("ready to send")
            val = str(r.value)
            print(val)
            await websocket.send(val)
            print("sent")
        except:
            print("breaking")
            break

start_server = websockets.serve(hello, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

# the callback will now be fired upon receipt of new values

def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        connection.stop()
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.pause()
