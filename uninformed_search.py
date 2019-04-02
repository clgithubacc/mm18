def depthFirstSearch1(problem):
    dir=[]
    currentState=problem.getStartState()
    lastDirection=Directions.STOP
    visited=[]
    checkList=util.Stack()
    currentLevel=0
    while True:
        visited.append(currentState)
        if problem.isGoalState(currentState):
            break
        for successor in problem.getSuccessors(currentState):
            if successor[1]!=Directions.REVERSE[lastDirection] and successor[0] not in visited:
                    checkList.push([currentLevel+1,successor])

        nextElement=checkList.pop()
        currentState=nextElement[1][0]
        currentLevel=nextElement[0]
        dir=dir[:currentLevel-1]
        dir.append(nextElement[1][1])
        lastDirection=nextElement[1][1]
    return dir
def depthFirstSearch(problem):
    dir=[]
    startState=problem.getStartState()
    currentState=startState
    visited=[]
    checkList=util.Stack()
    firstRun=True
    potentialGoals=[]
    while True:
        visited.append(currentState)
        #if problem.isGoalState(currentState):
        #    break
        successors=problem.getSuccessors(currentState)
        isCandidate=len(successors)==3
        candidateSuccessors=[]
        for successor in successors:
            if successor[0] not in visited:
                checkList.push(successor)
                if isCandidate:
                    candidateSuccessors.append(successor[0])
        print '@',
        print dir
        print 'current checkList',
        print checkList.list
        if isCandidate and len(candidateSuccessors)==2:
            potentialGoals.append([currentState,candidateSuccessors])
        if not firstRun and checkList.isEmpty():
             break
        firstRun=False
        nextCell=checkList.pop()
        nextState=nextCell[0]
        path=searchPathTo(problem,currentState,nextState)
        print '$',
        print nextState,
        print path
        currentState=nextState
        dir.extend(path)
    #End of maze exploration
    dir.append(Directions.STOP)
    dir.append(Directions.STOP)
    #2.Back to start point
    path=searchPathTo(problem,currentState,startState)
    dir.extend(path)
    dir.append(Directions.STOP)
    dir.append(Directions.STOP)
    #3.Find goal position
    goalState=(0,0)
    hasFoundGoal=False
    for candidate in potentialGoals:
        candidateState=candidate[0]
        candidateSuccessors=candidate[1]
        L2Successors=[]
        for successor in problem.getSuccessors(candidateSuccessors[0]):
            successorState=successor[0]
            if successorState!=candidateState:
                L2Successors.append(successorState)
            
        for successor in problem.getSuccessors(candidateSuccessors[1]):
            if successor[0] in L2Successors:
                goalState=candidateState
                hasFoundGoal=True
                break
        if hasFoundGoal:
            break
    print '*Goal',
    print goalState
    #3.Find the shortest path to goal
    path=searchPathTo(problem,startState,goalState)
    
    dir.extend(path)
    return dir

def searchPathTo(problem,start,goal):
    print '!',
    print start,
    print goal
    dir=[]
    currentState=start
    lastDirection=Directions.STOP
    visited=[]
    checkList=util.Queue()
    currentLevel=0
    parent={}
    goalState=start
    while True:
        visited.append(currentState)
        if currentState == goal:
            goalState=currentState
            break
        for successor in problem.getSuccessors(currentState):
            if successor[1]!=Directions.REVERSE[lastDirection] and successor[0] not in visited:
                    checkList.push([currentLevel+1,successor])
                    parent[successor[0]]=[currentState,successor[1]]
            print successor,
        print 'End'
        nextElement=checkList.pop()
        currentState=nextElement[1][0]
        print currentState
        currentLevel=nextElement[0]
        lastDirection=nextElement[1][1]

    while goalState != start:
        dir.insert(0,parent[goalState][1])
        goalState=parent[goalState][0]
    return dir

def breadthFirstSearch(problem):
    dir=[]
    currentState=problem.getStartState()
    lastDirection=Directions.STOP
    visited=[]
    checkList=util.Queue()
    currentLevel=0
    parent={}
    goalState=(1,1)
    while True:
        visited.append(currentState)
        if problem.isGoalState(currentState):
            goalState=currentState
            break
        for successor in problem.getSuccessors(currentState):
            if successor[1]!=Directions.REVERSE[lastDirection] and successor[0] not in visited:
                    checkList.push([currentLevel+1,successor])
                    parent[successor[0]]=[currentState,successor[1]]
        nextElement=checkList.pop()
        currentState=nextElement[1][0]
        currentLevel=nextElement[0]
        lastDirection=nextElement[1][1]

    while goalState != problem.getStartState():
        dir.insert(0,parent[goalState][1])
        goalState=parent[goalState][0]
    return dir

def uniformCostSearch(problem,start,end):
    from game import Directions
    dir=[]
    currentState=problem.getStartState()
    lastDirection=Directions.STOP
    visited=[]
    checkList=util.PriorityQueue()
    currentLevel=0
    parent={}
    goalState=(1,1)
    cost=0
    while True:
        visited.append(currentState)
        if problem.isGoalState(currentState):
            goalState=currentState
            break
        for successor in problem.getSuccessors(currentState):
            if successor[1]!=Directions.REVERSE[lastDirection] and successor[0] not in visited:
                    checkList.push([currentLevel+1,successor,cost+problem.getCostOfActions([successor[1]])],cost+problem.getCostOfActions([successor[1]]))
                    parent[successor[0]]=[currentState,successor[1]]
                    #parent.update({successor[0],[currentState,successor[1]]})
        nextElement=checkList.pop()
        cost=nextElement[2]
        currentState=nextElement[1][0]
        currentLevel=nextElement[0]
        lastDirection=nextElement[1][1]

    while goalState != problem.getStartState():
        dir.insert(0,parent[goalState][1])
        goalState=parent[goalState][0]
    return dir

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
ucs = uniformCostSearch
