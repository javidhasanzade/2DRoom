import math
from Line import Line
from Point import Point

lines: list[Line] = [Line(Point(1, -1), Point(1, 1)),
                     Line(Point(2, -1), Point(2, 1)),
                     Line(Point(2, 3), Point(6, 3)),
                     Line(Point(-5, 0), Point(1, 0))]

inputDegree: int = 0
XP0: int = 0
YP0: int = 0


def solution(xp0: int, yp0: int, input_degree: int, l_lines: list[Line]) -> Line:
    current_min: int = 2147483647  # Integer max size
    return_id: int = 0
    degree: float = math.radians(input_degree)
    max_dist: int = 2147483647  # Integer max size

    for segment in l_lines:
        end_y: int = segment.end.y
        end_x: int = segment.end.x
        st_y: int = segment.start.y
        st_x: int = segment.start.x
        lid: int = l_lines.index(segment)

        for i in range(1, max_dist, 1):
            YP: int = int(yp0 + (i * math.sin(degree)))
            XP: int = int(xp0 + (i * math.cos(degree)))
            if not(i < current_min):
                break
            if end_x == st_x:
                if XP == st_x:
                    current_min = i
                    return_id = lid
                    break
            elif end_y == st_y:
                if YP == st_y:
                    current_min = i
                    return_id = lid
                    break
            elif YP == ((end_y - st_y) / (end_x - st_x)) * XP + (st_y - ((end_y - st_y) / (end_x - st_x)) * st_x):
                current_min = i
                return_id = lid
                break

    return l_lines.__getitem__(return_id)


print(solution(XP0, YP0, inputDegree, lines))