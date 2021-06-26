class Boundaries:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def __contains__(self, coord):
        x, y = coord
        return 0 <= x < self.width and 0 <= y < self.height


class Grid:
    def __init__(self, width, height) -> None:
        self.width = width
        self.heigt = height
        self.limits = Boundaries(width, height)

    def __contains__(self, coord):
        return coord in self.limits


def mark_coordinate(grid, coord):
    if coord in grid:
        grid[coord] = "MARKED"
