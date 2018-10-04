from direction import Directions
from motor import turn
from motor import go
import time
# move(direction)
# move the robot for one cell in the given direction
# direction: A direction of type Directions

def move(carState, direction,numOfCell=1):
    #value=Directions.VALUE[direction]-Directions.VALUE[carState[1]]
    if carState[1]!=direction:
        turn(Directions.VALUE[(carState[1],direction)]*90)
        carState[1]=direction
    go(numOfCell)
    for i in range(0,numOfCell):
        carState[0]=carState[0].successors[direction]
    print('Move ',direction, 'for', numOfCell, 'cells. carState: ', carState)
    print('Pos after move: ',carState[0].position)



# listMove(listOfDir)
# execute a list of co

def listMove(carState, listOfDir):
    print('in listMove')
    index=0
    continuousCount=1
    while index<len(listOfDir)-1:
        if listOfDir[index+1]==listOfDir[index]:
            continuousCount+=1
            index+=1
            continue
        move(carState,listOfDir[index],continuousCount)
        continuousCount=1
        index+=1
    move(carState, listOfDir[index], continuousCount)
    #time.sleep(3)