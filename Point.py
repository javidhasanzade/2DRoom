class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point{x=" + self.x.__str__() + ", y=" + self.y.__str__() + "}"

