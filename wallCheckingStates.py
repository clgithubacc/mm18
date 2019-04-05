"""
States for wall detection. This is only used in new method (i.e. typeBasedMove)
Transitions:
AllWall -> BackHalfWall -> AllNonWall -> FrontHalfWall -> AllWall
"""
import _warnings
class WallCheckingStates_AllWall:
    def __init__(self, dirCount=0):
        self.dirCount=dirCount
    def nextState(self, frontValue, backValue):
        if frontValue==1 and backValue==1:
            return self
        elif frontValue==0 and backValue==1:
            return WallCheckingStates_BackHalfWall(self.dirCount)
        else:
            _warnings.warn('In State WallCheckingStates_Wall: Invalid state transitions ', frontValue, ' ',backValue)
            return self

class WallCheckingStates_BackHalfWall:
    def __init__(self):
        pass
    def nextState(self, frontValue, backValue):
        if frontValue==0 and backValue==1:
            return self
        elif frontValue==0 and backValue==0:
            return WallCheckingStates_AllNonWall(self.dirCount+1)
        else:
            _warnings.warn('In State WallCheckingStates_FrontHalf: Invalid state transitions ', frontValue, ' ',backValue)
            return self

class WallCheckingStates_AllNonWall:
    def __init__(self):
        pass
    def nextState(self, frontValue, backValue):
        if frontValue==0 and backValue==0:
            return self
        elif frontValue==1 and backValue==0:
            return WallCheckingStates_FrontHalfWall(self.dirCount)
        else:
            _warnings.warn('In State WallCheckingStates_NonWall: Invalid state transitions ', frontValue, ' ',backValue)
            return self

class WallCheckingStates_FrontHalfWall:
    def __init__(self):
        pass
    def nextState(self, frontValue, backValue):
        if frontValue==1 and backValue==0:
            return self
        elif frontValue==1 and backValue==0:
            return WallCheckingStates_AllWall(self.dirCount)
        else:
            _warnings.warn('In State WALL: Invalid state transitions ', frontValue, ' ',backValue)
            return self
