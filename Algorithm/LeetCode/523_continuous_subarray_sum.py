"""
# Problem Statement

Given a list of non-negative numbers and a target integer k, write a function to
check if the array has a continuous subarray of size at least 2 that sums up to
a multiple of k, that is, sums up to n*k where n is also an integer.

## Constraints:
The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.

# Examples
## Example 1:
Input: [23, 2, 4, 6, 7],  k=6 Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
## Example 2:
Input: [23, 2, 6, 4, 7],  k=6 Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
"""

def solution1(nums, K):
    # BF
    l = len(nums)
    for i in range(l):
        s = nums[i]
        for j in range(i+1, l):
            s += nums[j]
            if K != 0 and s % K == 0:
                return True
            if K == 0 and s == 0:
                return True
    return False

def solution2(nums, K):
    """sum_til record sum from begining
    sum between (i, j] sum_til[j] - sum_til[i]
    """
    s = 0
    sum_til = []
    for n in nums:
        s += n
        sum_til.append(s)

    l = len(nums)
    for i in range(l):
        for j in range(i+1, l):
            sum_ij = sum_til[j] if i == 0 else sum_til[j] - sum_til[i-1]
            if K != 0 and sum_ij % K == 0:
                return True
            if K == 0 and sum_ij == 0:
                return True
    return False

def solution3(nums, K):
    """if sum_ij is K*n --> sum_til[i-1] and sum_til[j] have the same modulus
    sum_til[i-1] % K == sum_til[j] % K
    """
    modSeen = {0:-1}
    s = 0
    for i in range(len(nums)):
        n = nums[i]
        s += n
        mod = s % K if K != 0 else s
        if mod in modSeen:
            if i - modSeen[mod] > 1:
                return True
        else:
            modSeen[mod] = i
    return False

import unittest
from unittest_data_provider import data_provider
from testdata.continuous_subarray_sum import TestData as data

class Tests(unittest.TestCase):
    @data_provider(data.basic)
    def test_solution1(self, nums, K, expected):
        self.assertEqual(expected, solution1(nums, K))

    @data_provider(data.big)
    def test_solution1_big_data(self, nums, K, expected):
        self.assertEqual(expected, solution1(nums, K))

    @data_provider(data.basic)
    def test_solution2(self, nums, K, expected):
        self.assertEqual(expected, solution2(nums, K))

    @data_provider(data.big)
    def test_solution2_big_data(self, nums, K, expected):
        self.assertEqual(expected, solution2(nums, K))

    @data_provider(data.basic)
    def test_solution3(self, nums, K, expected):
        self.assertEqual(expected, solution3(nums, K))

    @data_provider(data.big)
    def test_solution3_big_data(self, nums, K, expected):
        self.assertEqual(expected, solution3(nums, K))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Tests)
    unittest.TextTestRunner(verbosity=2).run(suite)
