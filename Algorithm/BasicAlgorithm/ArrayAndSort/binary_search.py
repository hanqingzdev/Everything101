def binarySearch(nums, target):
    nums.sort()

    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if nums[mid] > target:
            hi = mid - 1
        elif nums[mid] < target:
            lo = mid + 1
        else:
            return True

    return False


import unittest
from sort_test_base import SortTest
from unittest_data_provider import data_provider
import random

class BinarySearchTest(unittest.TestCase):
    @data_provider(SortTest.data)
    def test_basic_true(self, sortedNums, rawNums):
        for target in rawNums[:len(rawNums)//2]:
            self.assertTrue(binarySearch(sortedNums, target))

    @data_provider(SortTest.data)
    def test_basic_false(self, sortedNums, rawNums):
        for target in filter(lambda e: e not in rawNums, random.sample(range(100), 5)):
            self.assertFalse(binarySearch(sortedNums, target))

if __name__ == '__main__':
    unittest.main()
