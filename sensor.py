import serial
import time
def getSensorReading():
    '''
    Get readings from 3 sensors
    :return:  a list of 3 booleans in the order of [left, front, right] indicating whether there is a wall in that direction
    '''
    print ('Getting Readings:')
    time.sleep(0.5)
    ser = serial.Serial('/dev/ttyACM0', 9600)
    a='6'
    #print (a.encode())
    ser.write(a.encode())
    s=ser.read()
    input=int.from_bytes(s,byteorder='little')
    input-=48
    print('Input: ',input)
    #str=ser.readline()[2:3]
    #print (s)
    #print(input)
    #input=str(int(s,16))
    #num=int(input.decode())
    output={
        1:[0,0,0],
        2:[0,0,1],
        3:[0,1,0],
        4:[0,1,1],
        5:[1,0,0],
        6:[1,0,1],
        7:[1,1,0],
        8:[1,1,1]
    }
    print ('Sensor Reading:',output[input])
    return output[input]

def getBackSensorReadings():
    pass