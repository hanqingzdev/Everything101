"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

Follow up: Could you implement the O(n) solution?

* https://leetcode.com/problems/longest-consecutive-sequence/

Example 1:
Input: nums = [100,4,200,1,3,2] Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].  Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1] Output: 9

Constraints:

0 <= nums.length <= 104
-109 <= nums[i] <= 109
"""

def solution1(nums):
    l = len(nums)
    if l <= 1: return l

    nums.sort()
    max_l, curr_l = 1, 1
    for i in range(1, l):
        if nums[i] - nums[i-1] == 1:
            curr_l += 1
            max_l = max(max_l, curr_l)
        elif nums[i] - nums[i-1] == 0:
            pass
        else:
            curr_l = 1

    return max_l

def solution2(nums):
    """
    graph -> {} number: graph_index; graph[n] = graph_i; nums[graph[n]] == n -> it's the root
    find root: n -> graph_i = graph[n] -> nums[graph_i]
    """
    l = len(nums)
    graph = {}
    graph_size = {}
    def root_index(n):
        point_to_n = nums[graph[n]]
        if point_to_n == n:
            return graph[n]
        else:
            return root_index(point_to_n)

    max_size = 0
    for i in range(l):
        n = nums[i]
        if n in graph:
            continue
        root_i = i
        if n - 1 not in graph and n + 1 not in graph:
            graph[n] = i
        elif n - 1 in graph and n + 1 in graph:
            root_i1, root_i2 = root_index(n - 1), root_index(n + 1)
            graph[n] = root_i1
            root_i = root_i1
            if root_i1 != root_i2:
                graph[nums[root_i2]] = root_i1
                graph_size[root_i1] += graph_size[root_i2]
        else: # only one in graph
            n_in_graph = n - 1 if n - 1 in graph else n + 1
            graph[n] = graph[n_in_graph]
            root_i = root_index(n)

        # plus count
        graph_size[root_i] = (graph_size.get(root_i) or 0) + 1
        max_size = max(max_size, graph_size[root_i])

    return max_size

def solution3(nums):
    """convert nums to set -> for each n, continue searching n - 1 and n + 1"""
    s = set(nums)
    counted = set()
    max_size = 0

    def countStep(x, step):
        if x in s:
            counted.add(x)
            return countStep(x + step, step) + 1
        else:
            return 0

    for n in nums:
        if n in counted:
            continue
        size = countStep(n - 1, -1) + countStep(n + 1, 1) + 1
        max_size = max(max_size, size)
    return max_size


import unittest
from unittest_data_provider import data_provider

def data():
    #output, nums
    return [
        (3, [1,2,0,1]),
        (0, []),
        (1, [5]),
        (4, [100,4,200,1,3,2]),
        (9, [0,3,7,2,5,8,4,6,0,1]),
    ]

class Tests(unittest.TestCase):
    @data_provider(data)
    def test_solution1(self, expected, *argv):
        self.assertEqual(expected, solution1(*argv))

    @data_provider(data)
    def test_solution2(self, expected, *argv):
        self.assertEqual(expected, solution2(*argv))

    @data_provider(data)
    def test_solution3(self, expected, *argv):
        self.assertEqual(expected, solution3(*argv))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Tests)
    unittest.TextTestRunner(verbosity=2).run(suite)
