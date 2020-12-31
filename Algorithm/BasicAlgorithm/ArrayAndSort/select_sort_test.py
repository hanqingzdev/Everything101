import unittest
from sort_test_base import SortTest
from unittest_data_provider import data_provider
from select_sort import selectSort

class MergeSortTest(SortTest):
    @data_provider(SortTest.data)
    def test_basic(self, rst, nums):
        self.assertEqual(rst, selectSort(nums))

if __name__ == '__main__':
    unittest.main()
