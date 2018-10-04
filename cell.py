from direction import Directions


# Cell is equivalent to node in tree structure
class Cell:
    # pos is a list of size 2, where pos[0] is x, pos[1] is y
    # [new] pos should be a tuple (x,y)
    def __init__(self, pos):
        self.position = pos
        self.successors={Directions.NORTH:None,
                         Directions.SOUTH:None,
                         Directions.EAST:None,
                         Directions.WEST:None}
