"""
================================================================================
CHALLENGE: Maximum Depth of Binary Tree (LeetCode 104 / Medium)
TRACK: 08_linked_lists_trees_and_recursion
DIFFICULTY: Medium | POINTS: 20
================================================================================

PROBLEM STATEMENT:
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from
the root node down to the farthest leaf node.

Tree Node Definition:
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

INPUT FORMAT:
Level-order space-separated values ('null' for empty nodes).

SAMPLE INPUT 0:
3 9 20 null null 15 7

SAMPLE OUTPUT 0:
3
================================================================================
"""

import sys
from collections import deque
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Maximum Depth of Binary Tree"
POINTS = 20

TEST_CASES = [
    {"input": "3 9 20 null null 15 7\n", "expected": "3", "hidden": False},
    {"input": "1 null 2\n", "expected": "2", "hidden": False},
    {"input": "null\n", "expected": "0", "hidden": True}
]


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: TreeNode) -> int:
    # Hint: Return 0 if not root else 1 + max(max_depth(root.left), max_depth(root.right))
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
    raw = input().strip()
    if not raw or raw == "null":
        print(0)
        return
    nodes = raw.split()
    root = build_tree(nodes)
    print(max_depth(root))


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def max_depth(root: TreeNode) -> int:
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
================================================================================
"""
