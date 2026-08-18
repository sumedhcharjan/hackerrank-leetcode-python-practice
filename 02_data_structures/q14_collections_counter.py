"""
================================================================================
CHALLENGE: collections.Counter()
TRACK: 02_data_structures
DIFFICULTY: Easy | POINTS: 10
================================================================================

PROBLEM STATEMENT:
Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay x_i amount of money only if
they get the shoe of their desired size.

Your task is to compute how much money Raghu earned.

INPUT FORMAT:
The first line contains X, the number of shoes.
The second line contains space separated list of all shoe sizes in the shop.
The third line contains N, the number of customers.
The next N lines contain space separated values of desired shoe size and price offered.

SAMPLE INPUT 0:
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
5 55
8 200
10 40
6 20

SAMPLE OUTPUT 0:
200

EXPLANATION 0:
Customer 1: Purchased size 6 for $55. Remaining size 6: [6]
Customer 2: Purchased size 6 for $45. Remaining size 6: []
Customer 3: Purchased size 5 for $55.
Customer 4: Purchased size 8 for $200.
Customer 5: Size 10 not available -> No sale.
Customer 6: Size 6 not available -> No sale.
Total = 55 + 45 + 55 + 200 = 355 (Correction: Customer 1+2+3+4 = 355)
================================================================================
"""

import sys
from pathlib import Path
from collections import Counter

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "collections.Counter()"
POINTS = 10

TEST_CASES = [
    {
        "input": "10\n2 3 4 5 6 8 7 6 5 18\n6\n6 55\n6 45\n5 55\n8 200\n10 40\n6 20\n",
        "expected": "355",
        "hidden": False
    }
]


def solve():
    # num_shoes = int(input())
    # shoe_sizes = Counter(map(int, input().split()))
    # num_customers = int(input())
    # total_earned = 0
    # Process customers
    pass


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def solve():
    from collections import Counter
    num_shoes = int(input())
    shoe_sizes = Counter(map(int, input().split()))
    num_customers = int(input())
    total_earned = 0
    for _ in range(num_customers):
        size, price = map(int, input().split())
        if shoe_sizes[size] > 0:
            total_earned += price
            shoe_sizes[size] -= 1
    print(total_earned)
================================================================================
"""
