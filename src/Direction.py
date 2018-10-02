import enum


from src.Coordinate import Coordinate

# Enum representing the directions an ant can take.
class Direction(enum.Enum):
    east = 0
    north = 1
    west = 2
    south = 3

    # Get vector (coordinate) of a certain direction.
    # @param dir the direction
    # @return the coordinate
    @classmethod
    def dir_to_coordinate_delta(cls, dir):
        # all directions in a vector
        # Creates a map with a direction linked to its (direction) vector.
        map = {}
        map[cls.east] = Coordinate(1, 0)
        map[cls.west] = Coordinate(0, -1)
        map[cls.north] = Coordinate(-1, 0)
        map[cls.south] = Coordinate(0, 1)
        return map[dir]

    # Direction to an int.
    # @param dir the direction.
    # @return an integer from 0-3.
    @classmethod
    def dir_to_int(cls, dir):
        return dir.value