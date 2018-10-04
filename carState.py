from direction import Directions
class CarState:
    position = [0, 0]
    currentDir = Directions.STOP

    def __init__(self):
        print('car')
