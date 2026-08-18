"""
================================================================================
CHALLENGE: Merge Two Sorted Lists (LeetCode 21 / Medium)
TRACK: 08_linked_lists_trees_and_recursion
DIFFICULTY: Medium | POINTS: 20
================================================================================

PROBLEM STATEMENT:
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together
the nodes of the first two lists.

Return the head of the merged linked list.

Example:
Input:  list1 = 1 -> 2 -> 4, list2 = 1 -> 3 -> 4
Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4

INPUT FORMAT:
First line: space-separated integers for list1.
Second line: space-separated integers for list2.

OUTPUT FORMAT:
Space-separated integers of the merged sorted linked list.

SAMPLE INPUT 0:
1 2 4
1 3 4

SAMPLE OUTPUT 0:
1 1 2 3 4 4
================================================================================
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from test_helper import run_tests

TITLE = "Merge Two Sorted Lists"
POINTS = 20

TEST_CASES = [
    {
        "input": "1 2 4\n1 3 4\n",
        "expected": "1 1 2 3 4 4",
        "hidden": False
    },
    {
        "input": "2 5 8\n1 3 7 9\n",
        "expected": "1 2 3 5 7 8 9",
        "hidden": True
    }
]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    # Hint: Use a dummy node and iterate comparing list1.val vs list2.val
    pass


def build_linked_list(arr: list) -> ListNode:
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def linked_list_to_list(head: ListNode) -> list:
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res


def solve():
    line1 = input().strip()
    line2 = input().strip()
    arr1 = list(map(int, line1.split())) if line1 else []
    arr2 = list(map(int, line2.split())) if line2 else []
    
    l1 = build_linked_list(arr1)
    l2 = build_linked_list(arr2)
    
    merged = merge_two_lists(l1, l2)
    res_arr = linked_list_to_list(merged)
    print(" ".join(map(str, res_arr)))


if __name__ == '__main__':
    run_tests(solve, TEST_CASES, TITLE)


"""
================================================================================
SOLUTION HINT:
--------------------------------------------------------------------------------
def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode(0)
    curr = dummy
    while list1 and list2:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
    curr.next = list1 if list1 else list2
    return dummy.next
================================================================================
"""
