"""
* https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Notice that you may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
"""

def max_profit_unlimited(prices, i, j):
    # max profit between i and j with unlimited transcations
    steps = 0
    for x in range(i + 1, j + 1):
        steps += max(0, prices[x] - prices[x - 1])
    return steps

def max_profit_ij(prices, i, j):
    # max profit with at most 1 transcation from day 0 to day i
    l = len(prices)
    if i < 0 or i >= l or j < 0 or j >= l or j <= i:
        return 0
    lowest = prices[i]
    max_profit = 0
    for x in range(i, j + 1):
        price = prices[x]
        max_profit = max(max_profit, price - lowest)
        lowest = min(lowest, price)
    return max_profit

def solution1(k, prices):
    # divide conquer; Time O(2^N); Space(1); TLE
    l = len(prices)
    if l <= 1:
        return 0
    if 2 * k >= l:
        return max_profit_unlimited(prices, 0, l - 1)

    def max_profit_from_i(k, i):
        # max profit with at most k transactions from day i
        if k < 1:
            return 0
        elif k == 1:
            return max_profit_ij(prices, i, l - 1)

        max_profit = 0
        for j in range(i, l):
            max_profit_j = max_profit_ij(prices, i, j) + max_profit_from_i(k - 1, j)
            max_profit = max(max_profit, max_profit_j)
        return max_profit

    return max_profit_from_i(k, 0)

def solution2(k, prices):
    # Time: O(K*N); Space: O(K*N)
    l = len(prices)
    if l <= 1:
        return 0
    if 2 * k >= l:
        return max_profit_unlimited(prices, 0, l - 1)

    cash_by_k = [[0] * l for _ in range(k + 1) ]

    for k0 in range(1, k + 1):
        cash_last_around = cash_by_k[k0 - 1]
        cash_curr_around = cash_by_k[k0]

        max_profit_may_with_trans = cash_last_around[0]
        for today in range(1, l):
            yesterday = today - 1
            max_profit_may_with_trans = max(
                cash_last_around[today],
                max_profit_may_with_trans + prices[today] - prices[yesterday])
            cash_curr_around[today] = max(cash_curr_around[yesterday], max_profit_may_with_trans)

    return cash_by_k[-1][-1]

def solution3(k, prices):
    l = len(prices)
    if l <= 1 or k == 0:
        return 0
    if 2 * k >= l:
        return max_profit_unlimited(prices, 0, l - 1)

    def find_slop(start):
        i = start + 1
        while i < l and prices[i] >= prices[i - 1]:
            i += 1
        return (start, i - 1)

    slops = []
    i = 0
    while i < l:
        (start, end) = find_slop(i)
        if end > start:
            slops.append((start, end))
        i = end + 1

    while len(slops) > k:
        # one merge: two near slops with min profit lost
        min_merge_lost = float('inf')
        to_merge = (0, 1)
        for i in range(1, len(slops)):
            s1, s2 = slops[i - 1], slops[i]
            merge_lost = min(
                prices[s1[1]] - prices[s1[0]],
                prices[s2[1]] - prices[s2[0]],
                prices[s1[1]] - prices[s2[0]],)
            if merge_lost < min_merge_lost:
                min_merge_lost = merge_lost
                to_merge = (i - 1, i)

        s1, s2 = slops[to_merge[0]], slops[to_merge[1]]
        p1, p2 = prices[s1[1]] - prices[s1[0]], prices[s2[1]] - prices[s2[0]]
        p_merge = prices[s2[1]] - prices[s1[0]]

        if p_merge > p1 and p_merge > p2:
            merge_to = (s1[0], s2[1])
        else:
            merge_to = s1 if p1 > p2 else s2

        slops[to_merge[0]] = merge_to
        slops.pop(to_merge[1])

    return sum([prices[end] - prices[start] for (start, end) in slops])

import unittest
from unittest_data_provider import data_provider

def data():
    return [
        (2, 2, [2,4,1]),
        (7, 2, [3,2,6,5,0,3]),
        (0, 0, [1, 3]),
        (6, 2, [3,3,5,0,0,3,1,4]),
        (5, 1, [6,1,6,4,3,0,2]),
        (5, 1, [8,9,6,1,6,4,3,0,2]),
        (11, 2, [8,6,4,3,3,2,3,5,8,3,8,2,6]),
    ]

def big_data():
    return [
        (482, 11, [48,12,60,93,97,42,25,64,17,56,85,93,9,48,52,42,58,85,81,84,69,36,1,54,23,15,72,15,11,94]),
    ]

class Tests(unittest.TestCase):
    @data_provider(data)
    def test_all_solutions(self, expected, *argv):
        for n in range(1, 10):
            fn_name = 'solution' + str(n)
            if fn_name in globals():
                fn = globals()[fn_name]
                #print('Expect %s. Testing %s with input %s' % (str(expected), fn_name, str(argv)))
                self.assertEqual(expected, fn(*argv))

    @data_provider(big_data)
    def test_big_input(self, expected, *argv):
        self.assertEqual(expected, solution2(*argv))
        self.assertEqual(expected, solution3(*argv))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Tests)
    unittest.TextTestRunner(verbosity=2).run(suite)
