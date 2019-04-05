class Directions:
    NORTH = 'North'
    SOUTH = 'South'
    EAST = 'East'
    WEST = 'West'
    STOP = 'Stop'

    LEFT = {NORTH: WEST,
            SOUTH: EAST,
            EAST: NORTH,
            WEST: SOUTH,
            STOP: STOP}

    RIGHT = {WEST: NORTH,
             EAST: SOUTH,
             NORTH: EAST,
             SOUTH: WEST,
             STOP: STOP}

    REVERSE = {NORTH: SOUTH,
               SOUTH: NORTH,
               EAST: WEST,
               WEST: EAST,
               STOP: STOP}
    VALUE = {
        NORTH: 0,
        SOUTH: 1,
        EAST: 2,
        WEST: 3
    }

    DIRECTION = {
        0:NORTH,
        1:SOUTH,
        2:EAST,
        3:WEST
    }

    RELATIVE_VALUE = {(NORTH, EAST):1,
                      (NORTH,SOUTH):2,
                      (NORTH,WEST):-1,
                      (EAST,SOUTH):1,
                      (EAST,WEST):2,
                      (EAST,NORTH):-1,
                      (SOUTH,WEST):1,
                      (SOUTH,NORTH):2,
                      (SOUTH,EAST):-1,
                      (WEST,NORTH):1,
                      (WEST,EAST):2,
                      (WEST,SOUTH):-1}