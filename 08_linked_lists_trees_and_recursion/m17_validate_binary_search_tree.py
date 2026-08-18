"""
================================================================================
CHALLENGE: Validate Binary Search Tree (LeetCode 98 / Medium)
TRACK: 08_linked_lists_trees_and_recursion
DIFFICULTY: Medium | POINTS: 20
================================================================================

PROBLEM STATEMENT:
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

INPUT FORMAT:
Level-order space-separated values ('null' for empty nodes).

OUTPUT FORMAT:
Print True if valid BST, else False.

SAMPLE INPUT 0:
2 1 3

SAMPLE OUTPUT 0:
True

SAMPLE INPUT 1:
5 1 4 null null 3 6

SAMPLE OUTPUT 1:
False
================================================================================
"""

import sys
from collections import deque
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Validate Binary Search Tree"
POINTS = 20

TEST_CASES = [
    {"input": "2 1 3\n", "expected": "True", "hidden": False},
    {"input": "5 1 4 null null 3 6\n", "expected": "False", "hidden": False},
    {"input": "10 5 15 null null 6 20\n", "expected": "False", "hidden": True}
]


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: TreeNode) -> bool:
    # Hint: Use helper function valid(node, low_bound, high_bound)
    
    def help(node,low,up) -> bool:
        if(node==None):
            return True
        if(node.val<low or node.val>up):
            return False
        
        return help(node.left,low,node.val) and help(node.right,node.val,up)

    return help(root,float('-inf'),float('inf'))



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
        print(True)
        return
    nodes = raw.split()
    root = build_tree(nodes)
    print(is_valid_bst(root))


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def is_valid_bst(root: TreeNode) -> bool:
    def validate(node, low=float('-inf'), high=float('inf')):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return validate(node.left, low, node.val) and validate(node.right, node.val, high)
    return validate(root)
================================================================================
"""
