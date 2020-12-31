import unittest
from sort_test_base import SortTest
from unittest_data_provider import data_provider
from merge_sort import mergeSort

class MergeSortTest(SortTest):
    @data_provider(SortTest.data)
    def test_basic(self, rst, nums):
        self.assertEqual(rst, mergeSort(nums))

    @data_provider(SortTest.bigData)
    def test_big_input(self, rst, nums):
        self.assertEqual(rst, mergeSort(nums))

if __name__ == '__main__':
    unittest.main()
