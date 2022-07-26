import unittest
from main import solution
from Point import Point
from Line import Line


class SolutionTestCase(unittest.TestCase):
    def test1_solution(self):
        lines = [Line(Point(1, -1), Point(1, 1)),
                 Line(Point(2, -1), Point(2, 1))]
        xp = 0
        yp = 0
        degree = 0
        correct_output = 'Line : start=Point{x=1, y=-1}, end=Point{x=1, y=1}'
        result = solution(xp, yp, degree, lines)
        self.assertEqual(result.__str__(), correct_output)

    def test2_solution(self):
        lines = [Line(Point(-3, 0), Point(-1, 2)),
                 Line(Point(0, 2), Point(2, 2)),
                 Line(Point(4, 0), Point(4, 4)),
                 Line(Point(1, 3), Point(3, 3)),
                 Line(Point(1, 4), Point(3, 4)),
                 Line(Point(1, -3), Point(3, -1)),
                 Line(Point(2, -3), Point(3, -2)),
                 Line(Point(-4, 3), Point(-2, 2)),
                 Line(Point(-3, 1), Point(-2, -2)),
                 Line(Point(-4, -2), Point(-2, -4))]
        xp = 0
        yp = 0
        degree = 0
        correct_output = 'Line : start=Point{x=0, y=2}, end=Point{x=2, y=2}'
        result = solution(xp, yp, degree, lines)
        self.assertEqual(result.__str__(), correct_output)


if __name__ == '__main__':
    unittest.main()
