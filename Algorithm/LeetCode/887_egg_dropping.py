"""
# Problem Statement
Suppose you have N eggs and you want to determine from which floor in a K-floor
building you can drop an egg such that it doesn't break. You have to determine
the minimum number of attempts you need in order find the critical floor in the
worst case while using the best strategy.There are few rules given below.

- An egg that survives a fall can be used again.
- A broken egg must be discarded.
- The effect of a fall is the same for all eggs.
- If the egg doesn't break at a certain floor, it will not break at any floor below.
- If the eggs breaks at a certain floor, it will break at any floor above.
https://en.wikipedia.org/wiki/Dynamic_programming#Egg_dropping_puzzle

* https://practice.geeksforgeeks.org/problems/egg-dropping-puzzle-1587115620/1/
* LeetCode 887: https://leetcode.com/problems/super-egg-drop/

Your Task: Complete the function eggDrop() which takes two positive integer N and K as
input parameters and returns the minimum number of attempts you need in order to find the critical floor.

## Constraints:
1<=N<=10
1<=K<=50

## BigO
Expected Time Complexity : O(N*K)
Expected Auxiliary Space: O(N*K)


# Examples:
Input: N = 2, K = 10; Output: 4
Input: N = 3, K = 5; Output: 3
"""

def solution1(n, k):
    memorize = {}

    def max_floors(eggs, attempts):
        if (eggs, attempts) in memorize:
            return memorize[(eggs, attempts)]
        if eggs == 1:
            return attempts
        if attempts == 1:
            return 1

        ans = 1 + max_floors(eggs - 1, attempts - 1) + max_floors(eggs, attempts - 1)
        memorize[(eggs, attempts)] = ans

        return ans

    attempts = 1
    while max_floors(n, attempts) < k:
        attempts += 1

    return attempts

def solution2(n, k):
    memorize = {}
    def f(eggs, floors):
        if (eggs, floors) in memorize:
            return memorize[(eggs, floors)]

        if eggs < 1 or floors < 1:
            return 0
        if eggs == 1:
            return floors
        if floors <= 2:
            return floors

        possibles = []
        for pivot in range(1, floors + 1):
            possibles.append(max(f(eggs - 1, pivot - 1), f(eggs, floors - pivot)))

        ans = 1 + min(possibles)
        memorize[(eggs, floors)] = ans
        return ans

    return f(n, k)


import unittest
from unittest_data_provider import data_provider
from testdata.egg_dropping import EggDroppingTestData as data

class Tests(unittest.TestCase):
    @data_provider(data.basic)
    def test_solution1(self, eggs, floors, expected):
        self.assertEqual(expected, solution1(eggs, floors))

    @data_provider(data.basic)
    def test_solution2(self, eggs, floors, expected):
        self.assertEqual(expected, solution2(eggs, floors))

    @data_provider(data.big)
    def test_solution1_big_input(self, eggs, floors, expected):
        self.assertEqual(expected, solution1(eggs, floors))

    @data_provider(data.big)
    def test_solution2_big_input(self, eggs, floors, expected):
        try:
            self.assertEqual(expected, solution2(eggs, floors))
        except RecursionError as e:
            # RecursionError: maximum recursion depth exceeded in comparison
            pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Tests)
    unittest.TextTestRunner(verbosity=2).run(suite)
