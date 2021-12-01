import telnetlib
HOST = "192.168.43.174"
PORT = 80

ultrasonic = []


def sendCommands(commands):
    tn = telnetlib.Telnet(HOST,PORT)
    print(commands)
    print("Writing data")
    tn.write(commands)
    print("DISCONNECT")

def receiveData():
    tn = telnetlib.Telnet(HOST,PORT)
    print("Writing data")
    tn.write(b'RECEIVING')
    print("Reading data")
    data = tn.read_until(b'END').decode("utf-8") 
    print(data)
    ultrasonic.append(data[2])
    #print(ultrasonic)
    print("DISCONNECT")
    return data[2]







    
