"""
* https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/

Given an array of integers, return the maximum sum for a non-empty subarray
(contiguous elements) with at most one element deletion. In other words, you
want to choose a subarray and optionally delete one element from it so that
there is still at least one element left and the sum of the remaining elements
is maximum possible.

Note that the subarray needs to be non-empty after deleting one element.

Constraints:

    1 <= arr.length <= 10^5
    -10^4 <= arr[i] <= 10^4
"""

def solution1(arr):
    """ #TLE
    give a subArray -> sum[subArray] - smallest element (if it negative)
    """

    if len(arr) == 1:
        return arr[0]

    max_sum = float('-inf')
    l = len(arr)
    for i in range(l):
        for j in range(i, l):
            sub_arr = arr[i:j + 1]
            drop = min(min(sub_arr), 0) if j - i + 1 > 1 else 0
            max_sum = max(max_sum, sum(sub_arr) - drop)
    return max_sum

def solution2(arr):
    """improved solution1 #TLE """
    if len(arr) == 1:
        return arr[0]

    max_sum = float('-inf')
    l = len(arr)
    for i in range(l):
        local_sum = arr[i]
        local_min = arr[i]
        max_sum = max(max_sum, local_sum)

        for j in range(i + 1, l):
            local_sum += arr[j]
            local_min = min(local_min, arr[j])

            max_sum = max([max_sum, local_sum, local_sum - local_min])

    return max_sum

def solution3(arr):
    if len(arr) == 1:
        return arr[0]

    max_sum_with_no_del_up_here = [arr[0]]
    max_sum_with_one_del_up_here = [float('-inf')]
    max_sum = float('-inf')

    for i in range(1, len(arr)):
        max_sum_with_no_del_up_here.append(
            max(max_sum_with_no_del_up_here[i-1] + arr[i], arr[i]))
        max_sum_with_one_del_up_here.append(
            max(max_sum_with_no_del_up_here[i-1], max_sum_with_one_del_up_here[i-1] + arr[i]))
        max_sum = max(max_sum, max_sum_with_no_del_up_here[-1], max_sum_with_one_del_up_here[-1])

    return max_sum


import unittest
from unittest_data_provider import data_provider

def data():
    return [
        (5, [5]),
        (-5, [-5]),
        (4, [1,-2,0,3]),
        (3, [1,-2,-2,3]),
        (-1, [-1,-1,-1,-1]),
        (3, [2,1,-2,-5,-2]),
        (17, [-8,7,-12,-1,0,11,-2,-3,4,-13,2,3,-6]),
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
