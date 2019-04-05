from direction import Directions
import motorControl
import sensor
import wallCheckingStates
import time


# move(direction)
# move the robot for one cell in the given direction
# direction: A direction of type Directions
def move(carState, direction, numOfCell=1):
    # value=Directions.VALUE[direction]-Directions.VALUE[carState[1]]
    if carState[1] != direction:
        motorControl.turn(Directions.RELATIVE_VALUE[(carState[1], direction)] * 90)
        carState[1] = direction
    motorControl.go(numOfCell)
    for i in range(0, numOfCell):
        carState[0] = carState[0].successors[direction]
    print('Move ', direction, 'for', numOfCell, 'cells. carState: ', carState)
    print('Pos after move: ', carState[0].position)


# listMove(listOfDir)
# execute a list of co

def listMove(carState, listOfDir, moveType='old'):
    if moveType=='old':
        print('in listMove')
        index = 0
        continuousCount = 1
        while index < len(listOfDir) - 1:
            if listOfDir[index + 1] == listOfDir[index]:
                continuousCount += 1
                index += 1
                continue
            move(carState, listOfDir[index], continuousCount)
            continuousCount = 1
            index += 1
        move(carState, listOfDir[index], continuousCount)
        # time.sleep(3)
    elif moveType=='new':
        typeBasedList=generateTypeBasedList(carState[0], listOfDir)
        processPathList(typeBasedList)



def generateTypeBasedList(currentCell, listOfDir, debugMode=False):
    """
    Generate Type based list from direction based list
    :param currentCell: starting cell
    :param listOfDir: drection based list
    :return: a list of tuples of (Moving direction, (i.e. NSWE), Checking direction (i.e. Left/Center/Right), checking direction count, pathCount)
    """
    result = []
    # available paths on each direction along the current path, where current path has the same direction
    dirCount = [0, 0, 0, 0]
    lastCell = None
    movingDir = None
    directionCellCount = 1  # num of cells on the same direction
    for index in range(0, len(listOfDir)):
        currentDir = listOfDir[index]
        if debugMode:
            print('Result:', result)
        currentCell = currentCell.successors[currentDir]
        if currentCell is None:
            raise Exception("generateTypeBasedList: Next cell is None")
        if movingDir is None:
            # Start of a sequential movement
            movingDir = currentDir
            updatePathCount(currentCell, dirCount, movingDir)
        elif currentDir == movingDir:
            # Move in the same direction
            directionCellCount += 1
            updatePathCount(currentCell, dirCount, movingDir)
        else:
            # Differnt direction found. Save tuple to result and reset
            relativeDirection = Directions.RELATIVE_VALUE[(movingDir, currentDir)]  # Right: 1; Left: -1
            result.append((movingDir, relativeDirection, dirCount[Directions.VALUE[currentDir]],directionCellCount))
            dirCount = [0, 0, 0, 0]
            movingDir = currentDir
            directionCellCount = 1
            updatePathCount(lastCell, dirCount, movingDir)
            updatePathCount(currentCell, dirCount, movingDir)
        lastCell = currentCell
    if movingDir is not None:
        # add last element
        movingDirValue = Directions.VALUE[movingDir]
        minVal = 256
        minPos = -1
        for i in range(0, 4):
            if (dirCount[i] < minVal and dirCount[i] > 0):
                minVal = dirCount[i]
                minPos = i
        if minPos == -1:
            print(result)
            print(dirCount)
            raise Exception("In generateTypeBasedList(): Unable to handle last sequence of movement.")
        else:
            currentDir = Directions.DIRECTION[minPos]
            relativeDirection = Directions.RELATIVE_VALUE[(movingDir, currentDir)]  # Right: 1; Left: -1
            result.append((movingDir, relativeDirection, dirCount[Directions.VALUE[currentDir]]))
    return result


def updatePathCount(currentCell, pathCount, movingDir):
    """
    Update path count on each directions
    :param cell: current cell of type Cell
    :param pathCount: a list of int counting number of cells in North, South, Eash, and West in the path
    :param movingDir: current moving direction. Used for ignoring cells on moving direction and its reverse
    """
    isCountingNorthSouth = movingDir == Directions.WEST or movingDir == Directions.EAST
    if isCountingNorthSouth:
        if currentCell.successors[Directions.NORTH] is not None:
            pathCount[0] = pathCount[0] + 1
        if currentCell.successors[Directions.SOUTH] is not None:
            pathCount[1] = pathCount[1] + 1
    else:
        if currentCell.successors[Directions.EAST] is not None:
            pathCount[2] = pathCount[2] + 1
        if currentCell.successors[Directions.WEST] is not None:
            pathCount[3] = pathCount[3] + 1


def processPathList(carState, typeBasedList):
    for movingCommand in typeBasedList:
        movingDir, relativeDir, dirCount, pathLength = movingCommand
        motorControl.turn(Directions.RELATIVE_VALUE[(carState[1], movingDir)] * 90)
        carState[1]=movingDir
        #TODO: add auto correction function to handle frontSensor[0]!=backSensor[0]
        #TODO: update carState[0]

        #relativeDir+1: if check left, -1+1=0, if check right, 1+1=2
        initialSideValue=sensor.getSensorReading()[relativeDir+1]
        if initialSideValue==0:
            wallCheckingState=wallCheckingStates.WallCheckingStates_AllNonWall(1)
        else:
            wallCheckingState=wallCheckingStates.WallCheckingStates_AllWall(0)
        motorControl.fastGoForward(pathLength)
        while wallCheckingState.dirCount < dirCount:
            frontSensors = sensor.getSensorReading()
            backSensors = sensor.getBackSensorReadings()
            if relativeDir == -1:
                frontValue=frontSensors[0]
                backValue=backSensors[0]
            else:
                frontValue=frontSensors[3]
                backValue=backSensors[2]
            wallCheckingState=wallCheckingState.nextState(frontValue,backValue)
        #Enough dirCount. Stop car
        motorControl.stop()