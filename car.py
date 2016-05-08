import obd
import time
import signal
import sys

connection = obd.Async("/dev/ttyUSB0")

def new_rpm(r):
    if not r.is_null():
        print(str(r.value)+" "+str(r.unit)+"\r")

def new_fuel(r):
    if not r.is_null():
        print("Fuel: "+str(r.value)+" "+str(r.unit))

def new_tmp(r):
    if not r.is_null():
        print("Temp: "+str(r.value)+" "+str(r.unit))

def new_tmp2(r):
    if not r.is_null():
        print("Temp2: "+str(r.value)+" "+str(r.unit))

#connection.watch(obd.commands.RPM, callback=new_rpm)
connection.watch(obd.commands.SPEED, callback=new_rpm)
#connection.watch(obd.commands.INTAKE_TEMP, callback=new_tmp)
#connection.watch(obd.commands.THROTTLE_POS, callback=new_rpm)
connection.start()

# the callback will now be fired upon receipt of new values

def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        connection.stop()
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.pause()
