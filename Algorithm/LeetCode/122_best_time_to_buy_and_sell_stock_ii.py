"""
* https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many
transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:
Input: [7,1,5,3,6,4] Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

Example 2:
Input: [1,2,3,4,5] Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time.
You must sell before buying again.

Example 3:
Input: [7,6,4,3,1] Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Constraints:
1 <= prices.length <= 3 * 10 ^ 4
0 <= prices[i] <= 10 ^ 4
"""

def solution1(prices):
    # One pass O(N)
    l = len(prices)
    if l < 2:
        return 0

    last_lowest = prices[0]
    profit_sum = 0
    profit_curr = 0

    for i in range(1, len(prices)):
        p0, p1 = prices[i-1], prices[i]
        if p0 <= p1:
            continue
        else: # p0 > p1
            profit_sum += p0 - last_lowest # sell
            last_lowest = p1 # reset last_lowest

    if prices[-1] > last_lowest:
        profit_sum += prices[-1] - last_lowest

    return profit_sum

def solution2(prices):
    # DP; Track cash_if_buy_today/if_sell_today/if_no_action
    l = len(prices)
    if l < 2:
        return 0

    cash_if_buy = [-prices[0]]
    cash_if_sell = [0]
    cash_if_hold = [-prices[0]]
    cash_if_no_hold = [0]

    for i in range(1, l):
        p = prices[i]
        cash_if_buy.append(cash_if_no_hold[-1] - p)
        cash_if_sell.append(cash_if_hold[-1] + p)

        cash_if_hold.append(max(cash_if_buy[-1], cash_if_hold[-1]))
        cash_if_no_hold.append(max(cash_if_sell[-1], cash_if_no_hold[-1]))

    return cash_if_no_hold[-1]

def solution3(prices):
    # Find all slops and sum steps
    l = len(prices)
    if l <= 1:
        return 0

    def find_slop(i): # -> (steps, next_i after slop)
        i += 1
        steps = 0
        while i < l:
            if prices[i] > prices[i - 1]:
                steps += prices[i] - prices[i - 1]
                i += 1
            elif prices[i] == prices[i - 1]:
                i += 1
            else: # prices[i] < prices[i - 1]
                break
        return (steps, i)

    i = 0
    sum_steps = 0
    while i < l:
        steps, next_i = find_slop(i)
        sum_steps += steps
        i = next_i
    return sum_steps

def solution4(prices):
    # Simplified solution3
    steps = 0
    for i in range(1, len(prices)):
        steps += max(0, prices[i] - prices[i - 1])
    return steps



import unittest
from unittest_data_provider import data_provider

def data():
    return [
        (7, [7,1,5,3,6,4]),
        (4, [1,2,3,4,5]),
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
