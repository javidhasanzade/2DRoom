import math
import numpy as np
from Line import Line
from Point import Point

lines = [Line(Point(-3, 0), Point(-1, 2)),
         Line(Point(2, 0), Point(2, 2)),
         Line(Point(4, 0), Point(4, 4)),
         Line(Point(1, 3), Point(3, 3)),
         Line(Point(1, 4), Point(3, 4)),
         Line(Point(1, -3), Point(3, -1)),
         Line(Point(2, -3), Point(3, -2)),
         Line(Point(-4, 3), Point(-2, 2)),
         Line(Point(-3, 0), Point(-1, -2)),
         Line(Point(-4, -2), Point(-2, -4)),
         Line(Point(-3, -1), Point(-2, -2)),
         Line(Point(-1, 5), Point(1, 5)),
         Line(Point(-1, -5), Point(1, -5))]

inputDegree: int = 46
XP0: int = 0
YP0: int = 0


def crutch(x: float) -> float:
    _str: str = str(x)
    return float(_str[0:4])


def max_distance(line: Line, xp0: int, yp0: int):
    end_dist: int = int(math.sqrt(math.pow((line.end.y - yp0), 2) + math.pow((line.end.x - xp0), 2)))
    st_dist: int = int(math.sqrt(math.pow((line.start.y - yp0), 2) + math.pow((line.start.x - xp0), 2)))
    return max(end_dist, st_dist)


def solution(xp0: int, yp0: int, input_degree: int, l_lines: list[Line]) -> Line:
    current_min: float = 2147483647  # Integer max size
    return_id: int = -1
    degree: float = math.radians(input_degree)

    for segment in l_lines:
        end_y: int = segment.end.y
        end_x: int = segment.end.x
        st_y: int = segment.start.y
        st_x: int = segment.start.x
        lid: int = l_lines.index(segment)

        for i in np.arange(0, max_distance(segment, xp0, yp0) * 2 + 1, 0.01):
            i = round(i, 2)
            YP_exact: float = yp0 + (i * math.sin(degree))
            XP_exact: float = xp0 + (i * math.cos(degree))
            YP: int = int(YP_exact)
            XP: int = int(XP_exact)

            if not (i < current_min):
                break

            YP_exact_r: float = crutch(YP_exact)
            XP_exact_r: float = crutch(XP_exact)
            vert_cond = max(st_y, end_y) >= YP_exact_r >= min(st_y, end_y)
            hor_cond = max(st_x, end_x) >= XP_exact_r >= min(st_x, end_x)
            curve_cond = vert_cond and hor_cond

            # print(f"YP = {YP} YP_exact = {YP_exact} YP_exact_r = {round(YP_exact, 2)}")
            if end_x == st_x:
                if XP == st_x:
                    if not vert_cond:
                        continue
                    current_min = i
                    return_id = lid
                    break
            elif end_y == st_y:
                if YP == st_y:
                    if not hor_cond:
                        continue
                    current_min = i
                    return_id = lid
                    break
            elif YP_exact_r == (float((end_y - st_y) / (end_x - st_x)) * XP_exact_r + (end_y - (float((end_y - st_y) / (end_x - st_x)) * end_x))):
                if not curve_cond:
                    continue
                current_min = i
                return_id = lid
                break
    if return_id < 0:
        raise Exception("Not found")
    return l_lines.__getitem__(return_id)


try:
    print(solution(XP0, YP0, inputDegree, lines))
except Exception as e:
    print(e)
