import unittest
from main import solution
from Point import Point
from Line import Line


class SolutionTestCase(unittest.TestCase):
    def test_solution(self):
        lines = [Line(Point(1, -1), Point(1, 1)),
                 Line(Point(2, -1), Point(2, 1))]
        xp = 0
        yp = 0
        degree = 0
        correct_output = 'Line : start=Point{x=1, y=-1}, end=Point{x=1, y=1}'
        result = solution(xp, yp, degree, lines)
        self.assertEqual(result.__str__(), correct_output)


if __name__ == '__main__':
    unittest.main()
