"""
* https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
"""

def solution1(prices):
    # Time: O(N); Space: O(N)
    l = len(prices)
    if l < 2:
        return 0

    max_profit_from_left_until_today = [0]
    lowest_from_left = prices[0]
    max_profit_from_left = 0

    for i in range(1, l):
        price = prices[i]
        profit = price - lowest_from_left
        max_profit_from_left = max(max_profit_from_left, profit)
        lowest_from_left = min(lowest_from_left, price)

        max_profit_from_left_until_today.append(max_profit_from_left)

    max_profit_from_right_start_toady = [0]
    highest_from_right = prices[-1]
    max_profit_from_right = 0
    for i in range(l-2, -1, -1):
        price = prices[i]
        profit = highest_from_right - price

        max_profit_from_right = max(max_profit_from_right, profit)
        highest_from_right = max(highest_from_right, price)

        max_profit_from_right_start_toady.insert(0, max_profit_from_right)

    max_profit = 0
    for i in range(1, l):
        max_from_left = max_profit_from_left_until_today[i-1]
        max_from_right = max_profit_from_right_start_toady[i]

        max_profit = max(max_profit, max_from_left + max_from_right)

    return max(max_profit, max_profit_from_left_until_today[-1],  max_profit_from_right_start_toady[0])

def solution2(prices):
    # Time: O(N^2); Space: O(1)

    def max_profit(prices):
        l = len(prices)
        if l < 2:
            return 0
        lowest = prices[0]
        max_profit = 0
        for i in range(1, l):
            max_profit = max(max_profit, prices[i] - lowest)
            lowest = min(lowest, prices[i])
        return max_profit

    max_p = 0
    for i in range(len(prices)):
        max_p = max(max_p, max_profit(prices[:i]) + max_profit(prices[i:]))

    return max_p

def solution3(prices):
    # Improved solution2
    # Time: O(N); Space: O(N)

    max_profits_left = {} # i: (max_profit, lowest_price)
    def get_max_profit_left(i):
        if i < 0 or i >= len(prices):
            return (0, float('-inf'))
        if i in max_profits_left:
            return max_profits_left[i]
        if i == 0:
            max_profits_left[i] = (0, prices[i])
        else:
            sub_max, lowest = get_max_profit_left(i - 1)
            price = prices[i]
            max_profits_left[i] = (max(sub_max, price - lowest), min(lowest, price))
        return max_profits_left[i]

    max_profits_right = {} # i: (max_profit, highest_price)
    def get_max_profit_right(i):
        if i < 0 or i >= len(prices):
            return (0, float('inf'))
        if i in max_profits_right:
            return max_profits_right[i]
        if i == len(prices) - 1:
            max_profits_right[i] = (0, prices[i])
        else:
            sub_max, highest = get_max_profit_right(i + 1)
            price = prices[i]
            max_profits_right[i] = (max(sub_max, highest - price), max(highest, price))
        return max_profits_right[i]

    l = len(prices)
    if l < 2:
        return 0

    max_p = 0
    for i in range(l):
        max_p = max(max_p, get_max_profit_left(i)[0] + get_max_profit_right(i+1)[0])

    return max_p



import unittest
from unittest_data_provider import data_provider

def data():
    return [
        (6, [3,3,5,0,0,3,1,4,1]),
        (6, [3,3,5,0,0,3,1,4]),
        (4, [1,2,3,4,5]),
        (0, [7,6,4,3,1]),
        (0, [1]),
        (13, [1,2,4,2,5,7,2,4,9,0]),
    ]

class Tests(unittest.TestCase):
    @data_provider(data)
    def test_all_solutions(self, expected, *argv):
        for n in range(1, 10):
            fn_name = 'solution' + str(n)
            if fn_name in globals():
                fn = globals()[fn_name]
                # print('Testing %s with input %s' % (fn_name, str(argv)))
                self.assertEqual(expected, fn(*argv))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Tests)
    unittest.TextTestRunner(verbosity=2).run(suite)
