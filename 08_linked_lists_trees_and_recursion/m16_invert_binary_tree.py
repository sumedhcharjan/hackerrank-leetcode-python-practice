"""
================================================================================
CHALLENGE: Invert Binary Tree (LeetCode 226 / Medium)
TRACK: 08_linked_lists_trees_and_recursion
DIFFICULTY: Medium | POINTS: 20
================================================================================

PROBLEM STATEMENT:
Given the root of a binary tree, invert the tree (mirror image), and return its root.

Example:
Input:  4 2 7 1 3 6 9
Output: 4 7 2 9 6 3 1

INPUT FORMAT:
Level-order space-separated values ('null' for empty nodes).

OUTPUT FORMAT:
Level-order space-separated values of the inverted tree.

SAMPLE INPUT 0:
4 2 7 1 3 6 9

SAMPLE OUTPUT 0:
4 7 2 9 6 3 1
================================================================================
"""

import sys
from collections import deque
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Invert Binary Tree"
POINTS = 20

TEST_CASES = [
    {"input": "4 2 7 1 3 6 9\n", "expected": "4 7 2 9 6 3 1", "hidden": False},
    {"input": "2 1 3\n", "expected": "2 3 1", "hidden": False}
]


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: TreeNode) -> TreeNode:
    # Hint: Swap root.left and root.right recursively
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


def tree_to_level_order(root: TreeNode) -> str:
    if not root:
        return ""
    res = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            res.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append("null")
    while res and res[-1] == "null":
        res.pop()
    return " ".join(res)


def solve():
    raw = input().strip()
    if not raw or raw == "null":
        print("")
        return
    nodes = raw.split()
    root = build_tree(nodes)
    inverted = invert_tree(root)
    print(tree_to_level_order(inverted))


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def invert_tree(root: TreeNode) -> TreeNode:
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root
================================================================================
"""
