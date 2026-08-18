"""
================================================================================
CHALLENGE: Lowest Common Ancestor of a BST (LeetCode 235 / Medium)
TRACK: 08_linked_lists_trees_and_recursion
DIFFICULTY: Medium | POINTS: 20
================================================================================

PROBLEM STATEMENT:
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of
two given nodes p and q in the BST.

"The lowest common ancestor is defined between two nodes p and q as the lowest node
in T that has both p and q as descendants (where we allow a node to be a descendant
of itself)."

INPUT FORMAT:
First line: level-order space-separated values for BST.
Second line: integer p.
Third line: integer q.

OUTPUT FORMAT:
Print the value of the Lowest Common Ancestor node.

SAMPLE INPUT 0:
6 2 8 0 4 7 9 null null 3 5
2
8

SAMPLE OUTPUT 0:
6
================================================================================
"""

import sys
from collections import deque
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Lowest Common Ancestor of a BST"
POINTS = 20

TEST_CASES = [
    {
        "input": "6 2 8 0 4 7 9 null null 3 5\n2\n8\n",
        "expected": "6",
        "hidden": False
    },
    {
        "input": "6 2 8 0 4 7 9 null null 3 5\n2\n4\n",
        "expected": "2",
        "hidden": False
    }
]


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root: TreeNode, p: int, q: int) -> TreeNode:
    # Hint: Use BST property! If p and q both < root.val, go left. If both >, go right. Else root is LCA.
    pass


def build_tree(level_order: list) -> TreeNode:
    if not level_order or level_order[0] == "null":
        return None
    root = TreeNode(int(level_order[0]))
    queue = deque([root])
    i = 1
    while queue and i < len(level_order):
        curr = queue.popleft()
        if i < len(level_order) and level_order[i] != "null":
            curr.left = TreeNode(int(level_order[i]))
            queue.append(curr.left)
        i += 1
        if i < len(level_order) and level_order[i] != "null":
            curr.right = TreeNode(int(level_order[i]))
            queue.append(curr.right)
        i += 1
    return root


def solve():
    nodes = input().strip().split()
    p = int(input())
    q = int(input())
    root = build_tree(nodes)
    lca = lowest_common_ancestor(root, p, q)
    print(lca.val if lca else "")


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def lowest_common_ancestor(root: TreeNode, p: int, q: int) -> TreeNode:
    curr = root
    while curr:
        if p < curr.val and q < curr.val:
            curr = curr.left
        elif p > curr.val and q > curr.val:
            curr = curr.right
        else:
            return curr
================================================================================
"""
