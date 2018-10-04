import os.path
mazeName="savedMaze"
visitedName="savedVisited"
def importStoredMaze():
    data = {}
    for i in range(0, 16):
        for j in range(0, 16):
            data[(i, j)] = None
    if os.path.isfile(mazeName):
        print("Load saved maze.")
        file=open(mazeName)
        tmp=file.readline()

    return data

def importStoredVisited():
    visited=[]
    if os.path.isfile(visitedName):
        print("Load saved maze.")
        file=open(visitedName)
    return visited