"""
================================================================================
CHALLENGE: Class 2 - Find the Torsional Angle (3D Vectors)
TRACK: 05_classes_and_oop
DIFFICULTY: Medium | POINTS: 20
================================================================================

PROBLEM STATEMENT:
You are given four points A, B, C and D in a 3-dimensional Cartesian coordinate system.
You are required to find the angle between the plane made by the points A, B, C and
B, C, D in degrees (torsional angle).

Let AB = B - A, BC = C - B, CD = D - C.
X = AB x BC (cross product)
Y = BC x CD (cross product)

cos(phi) = (X . Y) / (|X| * |Y|)

INPUT FORMAT:
One line of input containing space separated values of x, y, z for point A.
One line of input containing space separated values of x, y, z for point B.
One line of input containing space separated values of x, y, z for point C.
One line of input containing space separated values of x, y, z for point D.

OUTPUT FORMAT:
Output the angle in degrees formatted to 2 decimal places.

SAMPLE INPUT 0:
0 4 5
1 7 6
0 5 9
1 7 2

SAMPLE OUTPUT 0:
8.19
================================================================================
"""

import sys
import math
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Find the Torsional Angle"
POINTS = 20

TEST_CASES = [
    {
        "input": "0 4 5\n1 7 6\n0 5 9\n1 7 2\n",
        "expected": "8.19",
        "hidden": False
    }
]


class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        return Points(self.x - no.x, self.y - no.y, self.z - no.z)

    def dot(self, no):
        return self.x * no.x + self.y * no.y + self.z * no.z

    def cross(self, no):
        return Points(
            self.y * no.z - self.z * no.y,
            self.z * no.x - self.x * no.z,
            self.x * no.y - self.y * no.x
        )
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


def solve():
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(Points(*a))

    a, b, c, d = points[0], points[1], points[2], points[3]

    ab = b - a
    bc = c - b
    cd = d - c

    x = ab.cross(bc)
    y = bc.cross(cd)

    cos_phi = x.dot(y) / (x.absolute() * y.absolute())
    res = math.degrees(math.acos(cos_phi))
    print("%.2f" % res)


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
The solve function contains the vector math implementation.
Ensure dot product and cross product magic methods return Points objects correctly.
================================================================================
"""
