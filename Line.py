from Point import Point


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def __str__(self):
        return "Line : " + "start=" + self.start.__str__() + ", end=" + self.end.__str__()
