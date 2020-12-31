"""
* https://leetcode.com/problems/split-array-largest-sum/
Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.
"""

def solution1(nums, m):
    # Time O(N^m); Space O(1)
    def fn(nums, m):
        l = len(nums)
        if m == 1:
            return sum(nums)
        if m == l:
            return max(nums)
        min_max_sum = float('inf')
        leading_sum = 0
        for i in range(l):
            leading_sum += nums[i]
            sub_max_sum = fn(nums[i+1:], m - 1)
            min_max_sum = min(min_max_sum, max(leading_sum, sub_max_sum))

        return min_max_sum

    return fn(nums, m)




import unittest
from unittest_data_provider import data_provider

def data():
    return [
        (18, [7,2,5,10,8], 2),
        (9, [1,2,3,4,5], 2),
        (4, [1,4,4], 3),
        (29, [2,16,14,15], 2),
    ]

class Tests(unittest.TestCase):
    @data_provider(data)
    def test_all_solutions(self, expected, *argv):
        for n in range(1, 10):
            fn_name = 'solution' + str(n)
            if fn_name in globals():
                fn = globals()[fn_name]
                #print('Testing %s with input %s' % (fn_name, str(argv)))
                self.assertEqual(expected, fn(*argv))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Tests)
    unittest.TextTestRunner(verbosity=2).run(suite)
