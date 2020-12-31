"""
# Problem
Given an array nums of n integers and an integer target, find three integers in
nums such that the sum is closest to target. Return the sum of the three
integers. You may assume that each input would have exactly one solution.

* LeetCode 16 https://leetcode.com/problems/3sum-closest/

## Constraints:
3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4

# Example 1:
Input: nums = [-1,2,1,-4], target = 1 Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

def solution1(nums, target):
    # BF solution
    l = len(nums)
    min_delta = float('inf')
    ans = None
    for i in range(l):
        for j in range(i+1, l):
            for k in range(j+1, l):
                the_sum = nums[i] + nums[j] + nums[k]
                if abs(target - the_sum) < min_delta:
                    min_delta = abs(target - the_sum)
                    ans = the_sum
                if min_delta == 0:
                    return target
    return ans

def solution2(nums, target):
    # Two pointer 2Sum
    nums.sort()
    l = len(nums)
    min_delta = float('inf')
    ans = None

    for i in range(l):
        lo, hi = i+1, l-1

        while lo < hi:
            the_sum = nums[i] + nums[lo] + nums[hi]
            if abs(target - the_sum) < min_delta:
                min_delta = abs(target - the_sum)
                ans = the_sum
            if the_sum > target:
                hi -= 1
            elif the_sum < target:
                lo += 1
            else:
                return target

    return ans

def solution3(nums, target):
    # Binary search
    nums.sort()
    l = len(nums)
    min_delta = float('inf')
    ans = None

    for i in range(l):
        for j in range(i+1, l):
            lo, hi = j+1, l-1

            while lo <= hi:
                mid = lo + (hi - lo) // 2
                the_sum = nums[i] + nums[j] + nums[mid]

                if abs(target - the_sum) < min_delta:
                    min_delta = abs(target - the_sum)
                    ans = the_sum

                if the_sum > target:
                    hi = mid - 1
                elif the_sum < target:
                    lo = mid + 1
                else:
                    return target

    return ans

import unittest
from unittest_data_provider import data_provider
from testdata.three_sum_closest import TestData as data

class Tests(unittest.TestCase):
    @data_provider(data.basic)
    def test_solution1(self, nums, target, expected):
        self.assertEqual(expected, solution1(nums, target))

    @data_provider(data.basic)
    def test_solution2(self, nums, target, expected):
        self.assertEqual(expected, solution2(nums, target))

    @data_provider(data.basic)
    def test_solution3(self, nums, target, expected):
        self.assertEqual(expected, solution3(nums, target))

    """@data_provider(data.big)
    def test_solution1_big_data(self, nums, target, expected):
        self.assertEqual(expected, solution1(nums, target))"""

    @data_provider(data.big)
    def test_solution2_big_data(self, nums, target, expected):
        self.assertEqual(expected, solution2(nums, target))

    @data_provider(data.big)
    def test_solution3_big_data(self, nums, target, expected):
        self.assertEqual(expected, solution3(nums, target))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Tests)
    unittest.TextTestRunner(verbosity=2).run(suite)
