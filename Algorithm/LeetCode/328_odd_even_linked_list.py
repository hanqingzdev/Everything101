"""
# Problem Statement
Given a singly linked list, group all odd nodes together followed by the even
nodes. Please note here we are talking about the node number and not the value
in the nodes.

You should try to do it in place. The program should run in O(1) space
complexity and O(nodes) time complexity.

* https://leetcode.com/problems/odd-even-linked-list/

## Constraints:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
The length of the linked list is between [0, 10^4].

# Examples:
## Example 1:
Input: 1->2->3->4->5->NULL Output: 1->3->5->2->4->NULL
# Example 2:
Input: 2->1->3->5->6->4->7->NULL Output: 2->3->6->7->1->5->4->NULL
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solution1(root):
    odd = root
    even = root.next if root else None

    while even and even.next:
        to_move = even.next

        # remove to_move from even_tail
        even.next = to_move.next
        even = even.next
        # insert to_move after odd_tail
        to_move.next = odd.next
        odd.next = to_move
        odd = odd.next

    return root

def solution2(root):
    is_odd = 1
    odd, even = ListNode(), ListNode()
    odd_head, even_head = odd, even

    node = root
    while node:
        if is_odd == 1:
            odd.next = node
            odd = odd.next
        else:
            even.next = node
            even = even.next
        node = node.next
        is_odd = is_odd * -1
    odd.next = even_head.next
    even.next = None
    return odd_head.next

import unittest
from unittest_data_provider import data_provider
from testdata.odd_even_linked_list import TestData as data

def to_list(root):
    l = []
    while root:
        l.append(root.val)
        root = root.next
    return l

class Tests(unittest.TestCase):
    @data_provider(data.basic)
    def test_solution1(self, root, expected):
        self.assertEqual(to_list(expected), to_list(solution1(root)), str(to_list(root)))

    @data_provider(data.big)
    def test_solution1_big_data(self, root, expected):
        self.assertEqual(to_list(expected), to_list(solution1(root)), to_list(root))

    @data_provider(data.basic)
    def test_solution2(self, root, expected):
        self.assertEqual(to_list(expected), to_list(solution2(root)), str(to_list(root)))

    @data_provider(data.big)
    def test_solution2_big_data(self, root, expected):
        self.assertEqual(to_list(expected), to_list(solution2(root)), to_list(root))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Tests)
    unittest.TextTestRunner(verbosity=2).run(suite)
