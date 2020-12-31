"""
* https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another
solution using the divide and conquer approach, which is more subtle.
"""

def solution1(arr):
    # BF; O(N^2)
    max_sum = float('-inf')
    l = len(arr)
    for i in range(l):
        s = arr[i]
        max_sum = max(max_sum, s)
        for j in range(i + 1, l):
            s += arr[j]
            max_sum = max(max_sum, s)
    return max_sum

def solution2(arr):
    # DP; O(N)
    max_up_here = [arr[0]]
    max_sum = arr[0]

    for i in range(1, len(arr)):
        max_up_here.append(max(max_up_here[i-1] + arr[i], arr[i]))
        max_sum = max(max_up_here[-1], max_sum)

    return max_sum

def solution3(arr):
    # Divide and Conquer O(NlogN)
    def cross_sum(nums, i):
        l = len(nums)
        lo, hi = i - 1, i + 1

        left_max = 0 # by default, no element from left
        left_sum = 0
        while lo >= 0:
            left_sum += nums[lo]
            left_max = max(left_max, left_sum)
            lo -= 1

        right_max = 0
        right_sum = 0
        while hi < l:
            right_sum += nums[hi]
            right_max = max(right_max, right_sum)
            hi += 1

        return left_max + nums[i] + right_max

    def divide_conquer(nums):
        l = len(nums)
        if l == 0: return float('-inf')
        if l == 1: return nums[0]

        pivot = len(nums) // 2

        left = divide_conquer(nums[:pivot])
        cross = cross_sum(nums, pivot)
        right = divide_conquer(nums[pivot+1:])
        return max(left, cross, right)

    return divide_conquer(arr)

def solution4(arr):
    # Greddy; O(N)
    max_sum = arr[0]
    curr_max = arr[0]

    for i in range(1, len(arr)):
        curr_max = max(curr_max + arr[i], arr[i])
        max_sum = max(max_sum, curr_max)
    return max_sum

import unittest
from unittest_data_provider import data_provider

def data():
    return [
        (6, [-2,1,-3,4,-1,2,1,-5,4]),
        (1, [1]),
        (0, [0]),
        (-1, [-1]),
        (-123, [-123]),
        (21, [8,-19,5,-4,20]),
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

    @data_provider(data)
    def test_solution4(self, expected, *argv):
        self.assertEqual(expected, solution4(*argv))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Tests)
    unittest.TextTestRunner(verbosity=2).run(suite)
