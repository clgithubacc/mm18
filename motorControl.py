import serial
import time
import sensor
while True:
    try:
        ser = serial.Serial('/dev/ttyACM0', 9600)
        break
    except:
        print('USB Disconnected. Reconnecting.')
        time.sleep(1)
def go(numOfCell=1):
    for i in  range(0,numOfCell):
        goForward()

def turn(degree):
    tmp=int(degree/90)
    print(tmp)
    if tmp<0:
        for i in range(tmp,0):
            
            turnLeft()
    elif tmp>0:
        for i in range(0,tmp):
            turnRight()


def goForward():
    time.sleep(1)
    a='2'
    print (a.encode())
    ser.write(a.encode())
    

def turnLeft():
    time.sleep(1.7)
    a='1'
    print (a.encode())
    ser.write(a.encode())

def turnRight():
    time.sleep(1.7)
    a='3'
    print (a.encode())
    ser.write(a.encode())

# def dirBasedMove(relativeDir, dirCount, pathLength):
#     """
#     Move object by counting paths on the given direction
#     :param relativeDir: checking left (-1) or right (1)
#     :param dirCount: number of non-wall cells on relativeDir
#     :param pathLength: length of the current path
#     """
#     fastGoForward(pathLength)
#     currentDirCount=0
#     while currentDirCount<dirCount:
#         frontSensors=sensor.getSensorReading()
#         backSensors=sensor.getBackSensorReadings()
#         if relativeDir==-1:


def fastGoForward(pathLength):
    modeNumber='4'
    ser.write(modeNumber.encode())

def stop():
    modeNumber='5'
    ser.write(modeNumber.encode())