"""
* https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one
and sell one share of the stock), design an algorithm to find the maximum
profit.

Note that you cannot sell a stock before you buy one.

Example 1:
Input: [7,1,5,3,6,4] Output: 5
Explanation:
Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2: Input: [7,6,4,3,1] Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

def solution1(prices):
    l = len(prices)
    if l < 2:
        return 0

    lowest_sofar = prices[0]
    max_profit = 0

    for p in prices[1:]:
        max_profit = max(max_profit, p - lowest_sofar)
        lowest_sofar = min(lowest_sofar, p)

    return max_profit



import unittest
from unittest_data_provider import data_provider

def data():
    return [
        (5, [7,1,5,3,6,4]),
        (0, [7,6,4,3,1]),
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
