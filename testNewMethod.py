from direction import Directions
from movement import generateTypeBasedList
from cell import Cell
testDirectionList=[('n',6),('e',1),('n',1),('w',1),('n',3),('e',1),('n',1),('w',1),('n',1),('e',2),('n',1),('w',2)]

def dirListDecoder(dirList):
    result=[]
    for item in dirList:
        if item[0]=='n':
            direction=Directions.NORTH
        elif item[0]=='s':
            direction=Directions.SOUTH
        elif item[0]=='w':
            direction=Directions.WEST
        elif item[0]=='e':
            direction=Directions.EAST
        else:
            print('illegal direction ', item[0], 'in input' )
            break
        for i in range(0,item[1]):
            result.append(direction)
    return result

def generateCell():
    start=Cell((1,1))
    start.successors[Directions.NORTH]=Cell((1,2))
    start.successors[Directions.NORTH].successors[Directions.REVERSE[Directions.NORTH]] = start
    currentCell=start.successors[Directions.NORTH]
    currentCell.successors[Directions.NORTH]=Cell((1,3))
    currentCell.successors[Directions.NORTH].successors[Directions.REVERSE[Directions.NORTH]] = currentCell
    currentCell=currentCell.successors[Directions.NORTH]
    currentCell.successors[Directions.NORTH]=Cell((1,4))
    currentCell.successors[Directions.NORTH].successors[Directions.REVERSE[Directions.NORTH]] = currentCell
    currentCell.successors[Directions.EAST]=Cell((2,4))
    currentCell.successors[Directions.EAST].successors[Directions.REVERSE[Directions.EAST]] = currentCell
    currentCell=currentCell.successors[Directions.NORTH]
    currentCell.successors[Directions.NORTH]=Cell((1,5))
    currentCell.successors[Directions.NORTH].successors[Directions.REVERSE[Directions.NORTH]] = currentCell
    currentCell=currentCell.successors[Directions.NORTH]
    currentCell.successors[Directions.NORTH]=Cell((1,6))
    currentCell.successors[Directions.NORTH].successors[Directions.REVERSE[Directions.NORTH]] = currentCell
    currentCell=currentCell.successors[Directions.NORTH]
    currentCell.successors[Directions.NORTH]=Cell((1,7))
    currentCell.successors[Directions.NORTH].successors[Directions.REVERSE[Directions.NORTH]] = currentCell
    currentCell=currentCell.successors[Directions.NORTH]

    nextDir=Directions.EAST
    currentCell.successors[nextDir]=Cell((2,7))
    currentCell.successors[nextDir].successors[Directions.REVERSE[nextDir]]=currentCell
    currentCell=currentCell.successors[nextDir]
    nextDir=Directions.NORTH
    currentCell.successors[nextDir]=Cell((2,8))
    currentCell.successors[nextDir].successors[Directions.REVERSE[nextDir]]=currentCell
    currentCell=currentCell.successors[nextDir]
    nextDir=Directions.NORTH
    currentCell.successors[nextDir]=Cell((2,9))
    currentCell.successors[nextDir].successors[Directions.REVERSE[nextDir]]=currentCell
    nextDir=Directions.WEST
    currentCell.successors[nextDir]=Cell((1,8))
    currentCell.successors[nextDir].successors[Directions.REVERSE[nextDir]]=currentCell
    currentCell=currentCell.successors[nextDir]
    nextDir=Directions.NORTH
    currentCell.successors[nextDir]=Cell((1,9))
    currentCell.successors[nextDir].successors[Directions.REVERSE[nextDir]]=currentCell
    currentCell=currentCell.successors[nextDir]
    nextDir=Directions.NORTH
    currentCell.successors[nextDir]=Cell((1,10))
    currentCell.successors[nextDir].successors[Directions.REVERSE[nextDir]]=currentCell
    currentCell=currentCell.successors[nextDir]
    nextDir=Directions.NORTH
    currentCell.successors[nextDir]=Cell((1,11))
    currentCell.successors[nextDir].successors[Directions.REVERSE[nextDir]]=currentCell
    currentCell=currentCell.successors[nextDir]
    nextDir=Directions.EAST
    currentCell.successors[nextDir]=Cell((2,11))
    currentCell.successors[nextDir].successors[Directions.REVERSE[nextDir]]=currentCell
    currentCell=currentCell.successors[nextDir]
    nextDir=Directions.NORTH
    currentCell.successors[nextDir]=Cell((2,12))
    currentCell.successors[nextDir].successors[Directions.REVERSE[nextDir]]=currentCell
    currentCell=currentCell.successors[nextDir]
    nextDir=Directions.WEST
    currentCell.successors[nextDir]=Cell((1,12))
    currentCell.successors[nextDir].successors[Directions.REVERSE[nextDir]]=currentCell
    currentCell=currentCell.successors[nextDir]
    nextDir=Directions.NORTH
    currentCell.successors[nextDir]=Cell((1,13))
    currentCell.successors[nextDir].successors[Directions.REVERSE[nextDir]]=currentCell
    currentCell=currentCell.successors[nextDir]
    nextDir=Directions.EAST
    currentCell.successors[nextDir]=Cell((2,13))
    currentCell.successors[nextDir].successors[Directions.REVERSE[nextDir]]=currentCell
    currentCell=currentCell.successors[nextDir]
    nextDir=Directions.EAST
    currentCell.successors[nextDir]=Cell((3,13))
    currentCell.successors[nextDir].successors[Directions.REVERSE[nextDir]]=currentCell
    currentCell=currentCell.successors[nextDir]
    nextDir=Directions.NORTH
    currentCell.successors[nextDir]=Cell((3,14))
    currentCell.successors[nextDir].successors[Directions.REVERSE[nextDir]]=currentCell
    currentCell=currentCell.successors[nextDir]
    nextDir=Directions.WEST
    currentCell.successors[nextDir]=Cell((2,14))
    currentCell.successors[nextDir].successors[Directions.REVERSE[nextDir]]=currentCell
    currentCell=currentCell.successors[nextDir]
    nextDir=Directions.WEST
    currentCell.successors[nextDir]=Cell((1,14))
    currentCell.successors[nextDir].successors[Directions.REVERSE[nextDir]]=currentCell
    nextDir=Directions.NORTH
    currentCell.successors[nextDir]=Cell((1,15))
    currentCell.successors[nextDir].successors[Directions.REVERSE[nextDir]]=currentCell
    currentCell=currentCell.successors[nextDir]

    return start


print(generateTypeBasedList(generateCell(), dirListDecoder(testDirectionList)))