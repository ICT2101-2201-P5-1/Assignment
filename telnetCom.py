import time
import telnetlib

HOST = "192.168.10.105"
PORT = 80


def sendCommands(commands):
    tn = telnetlib.Telnet(HOST,PORT)
    print(commands)
    print("Writing data")
    tn.write(commands)

    print("DISCONNECT")

def receiveData():
    tn = telnetlib.Telnet(HOST,PORT)
    print("RECEIVING!")
    #tn.write(B'RECEIVING')
    data = tn.read_until(b"END")
    print(data)
    print("DISCONNECT")
