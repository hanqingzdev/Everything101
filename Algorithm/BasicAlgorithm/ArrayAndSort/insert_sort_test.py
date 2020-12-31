import unittest
from sort_test_base import SortTest
from unittest_data_provider import data_provider
from insert_sort import insertSort1, insertSort2

class InsertSortTest(SortTest):
    @data_provider(SortTest.data)
    def test_basic_impl1(self, rst, nums):
        self.assertEqual(rst, insertSort1(nums))

    @data_provider(SortTest.data)
    def test_basic_impl2(self, rst, nums):
        self.assertEqual(rst, insertSort2(nums))
if __name__ == '__main__':
    unittest.main()
