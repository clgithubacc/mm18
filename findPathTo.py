#   A Breadth First Search from startCell to endCell based on known graph
#   @param  startCell, endCell - Cell object
#   @return a list of actions of type Directions
from queue import Queue
from direction import Directions
def findPathToCell(startCell,endCell):
    """
    Generate directions that guide the mouse from startCell to endCell in the shortest path
    :return: a list of directions of type Directions
    """
    dir = []
    startState=startCell.position
    terminateState=startState
    goal=endCell.position
    currentState=startCell
    lastDirection=Directions.STOP
    visited=[]
    checkList=Queue()
    currentLevel=0
    parent={}

    while True:
        visited.append(currentState.position)
        #print ('&')
        #print(currentState.position)
        #print(goal)
        if currentState.position==goal:
            terminateState=currentState.position
            break
        print(currentState.successors)
        for element in currentState.successors:
            direction=element
            cell=currentState.successors[direction]
            print(cell)
            if cell is not None:
                cellPos = cell.position
                if cellPos not in visited:
                    checkList.put([currentLevel + 1, cell, direction])
                    parent[cellPos] = [currentState.position, direction]

        nextCell=checkList.get()
        currentState=nextCell[1]
        currentLevel=nextCell[0]
        lastDirection=nextCell[2]

    while terminateState!=startState:
        #print(terminateState)
        #print(startState)
        dir.insert(0,parent[terminateState][1])
        terminateState=parent[terminateState][0]
    return dir

def findCell(goalPos,cell):
    """
    Find the cell with the coordinate of goalPos
    :param goalPos:  a tuple indicating coordinate
    :param cell:  starting cell
    :return:  the cell with the coordinate of goalPos. Return None if not found
    """
    checkList=Queue()
    currentCell=cell
    while currentCell.position != goalPos:
        for direction,successor in currentCell.successors:
            if successor is not None:
                checkList.put(successor)
        currentCell=checkList.get()
    if currentCell.position==goalPos:
        return currentCell
    else:
        return None