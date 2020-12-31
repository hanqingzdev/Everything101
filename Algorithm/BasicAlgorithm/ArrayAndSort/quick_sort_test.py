import unittest
from sort_test_base import SortTest
from unittest_data_provider import data_provider
from quick_sort import quickSort

class MergeSortTest(SortTest):
    @data_provider(SortTest.data)
    def test_basic(self, rst, nums):
        self.assertEqual(rst, quickSort(nums))

    @data_provider(SortTest.bigData)
    def test_big_input(self, rst, nums):
        self.assertEqual(rst, quickSort(nums))

if __name__ == '__main__':
    unittest.main()
