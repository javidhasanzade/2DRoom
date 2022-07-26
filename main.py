import math
from Line import Line
from Point import Point

lines: list[Line] = [Line(Point(1, -1), Point(1, 1)),
                     Line(Point(2, -1), Point(2, 1)),
                     Line(Point(2, 3), Point(6, 3))]

inputDegree: int = 0
XP0: int = 0
YP0: int = 0


def solution(XP_0: int, YP_0: int, input_degree: int, llines: list[Line]) -> Line:
    currentMin: int = 2147483647  # Integer max size
    returnId: int = 0
    degree: float = math.radians(input_degree)
    maxDist: int = 2147483647  # Integer max size

    for segment in llines:
        endY: int = segment.end.y
        endX: int = segment.end.x
        stY: int = segment.start.y
        stX: int = segment.start.x
        id: int = llines.index(segment)

        for i in range(1, maxDist, 1):
            YP: int = int(YP_0 + (i * math.sin(degree)))
            XP: int = int(XP_0 + (i * math.cos(degree)))
            if not(i < currentMin):
                break
            if endX == stX:
                if XP == stX:
                    currentMin = i
                    returnId = id
                    break
            elif endY == stY:
                if YP == stY:
                    currentMin = i
                    returnId = id
                    break
            elif YP == ((endY - stY) / (endX - stX)) * XP + (stY - ((endY - stY) / (endX - stX)) * stX):
                currentMin = i
                returnId = id
                break

    return llines.__getitem__(returnId)

print(solution(XP0, YP0, inputDegree, lines))