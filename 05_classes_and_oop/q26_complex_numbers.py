"""
================================================================================
CHALLENGE: Dealing with Complex Numbers (OOP & Magic Methods)
TRACK: 05_classes_and_oop
DIFFICULTY: Medium | POINTS: 20
================================================================================

PROBLEM STATEMENT:
For this challenge, you are given two complex numbers, and you have to print the
result of their addition, subtraction, multiplication, division and modulus operations.

Real and imaginary parts of a complex number can be expressed as: A + Bi.

Input Format:
One line of input for C = a + bi (separated by space).
One line of input for D = c + di (separated by space).

Output Format:
For two complex numbers C and D, print the results of:
C + D
C - D
C * D
C / D
mod(C)
mod(D)

Each formatted as `a.00 + b.00i` or `a.00 - b.00i`.

SAMPLE INPUT 0:
2 1
5 6

SAMPLE OUTPUT 0:
7.00 + 7.00i
-3.00 - 5.00i
4.00 + 17.00i
0.26 - 0.11i
2.24 + 0.00i
7.81 + 0.00i
================================================================================
"""

import sys
import math
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Dealing with Complex Numbers"
POINTS = 20

TEST_CASES = [
    {
        "input": "2 1\n5 6\n",
        "expected": "7.00 + 7.00i\n-3.00 - 5.00i\n4.00 + 17.00i\n0.26 - 0.11i\n2.24 + 0.00i\n7.81 + 0.00i",
        "hidden": False
    }
]


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        pass

    def __sub__(self, no):
        pass

    def __mul__(self, no):
        pass

    def __truediv__(self, no):
        pass

    def mod(self):
        pass

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f + %.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f - %.2fi" % (self.real, abs(self.imaginary))
        return result


def solve():
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        r = self.real * no.real - self.imaginary * no.imaginary
        i = self.real * no.imaginary + self.imaginary * no.real
        return Complex(r, i)

    def __truediv__(self, no):
        denom = no.real**2 + no.imaginary**2
        r = (self.real * no.real + self.imaginary * no.imaginary) / denom
        i = (self.imaginary * no.real - self.real * no.imaginary) / denom
        return Complex(r, i)

    def mod(self):
        return Complex(math.sqrt(self.real**2 + self.imaginary**2), 0)
================================================================================
"""
