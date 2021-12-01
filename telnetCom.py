import time
import telnetlib

HOST = "192.168.43.174"
PORT = 80


def sendCommands(commands):
    tn = telnetlib.Telnet(HOST,PORT)
    print(commands)
    print("Writing data")
    tn.write(commands)
    data = tn.read_until(b'END')
    print(data + "Recieved from Car")
    print("DISCONNECT")

def receiveData():
    tn = telnetlib.Telnet(HOST,PORT)
    print("Writing data")
    tn.write(b'RECEIVING')
    print("Reading data")
    data = tn.read_until(b'END')
    print("DISCONNECT")
    return data
