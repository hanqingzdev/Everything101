"""
# Problem Statement
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

* https://leetcode.com/problems/combination-sum-iii/

Example 1:
Input: k = 3, n = 7 Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7 There are no other valid combinations.

Example 2:
Input: k = 3, n = 9 Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

Example 3:
Input: k = 4, n = 1 Output: []
Explanation: There are no valid combinations. [1,2,1] is not valid because 1 is used twice.

Example 4:
Input: k = 3, n = 2 Output: []
Explanation: There are no valid combinations.

Example 5:
Input: k = 9, n = 45
Output: [[1,2,3,4,5,6,7,8,9]]
Explanation:
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
There are no other valid combinations.


## Constraints:

2 <= k <= 9
1 <= n <= 60
"""

"""
candidate: 1 -> 9
target: n
ans_len: k
"""

def solution1(k, n):
    def fn(nums, target, l):
        ans = []

        for i in range(len(nums)):
            n = nums[i]
            newTarget, newL = target - n, l - 1

            if newTarget == 0 and newL == 0:
                ans.append([n])
            elif newTarget > 0 and newL > 0 and i + 1 < len(nums):
                # nums[i+1:] len > 0 and target - n > 0 and l - 1 > 0
                subAns = fn(nums[i+1:], target - n, l - 1)
                for e in subAns:
                    ans.append([n] + e)
            else:
                pass # no answer
        return ans

    ans = fn(range(1, 10), n, k)

    return ans


import unittest
from unittest_data_provider import data_provider

def data():
    #output, k, n
    return [
        ( [[1,2,4]], 3, 7),
        ( [[1,2,6],[1,3,5],[2,3,4]], 3, 9),
        ( [], 4, 1),
        ( [], 3, 2),
        ( [[1,2,3,4,5,6,7,8,9]], 9, 45),
    ]

class Tests(unittest.TestCase):
    @data_provider(data)
    def test_solution1(self, expected, *argv):
        self.assertListIdentical(expected, solution1(*argv))

    def assertListIdentical(self, l1, l2):
        self.assertEqual(len(l1), len(l2))

        set1 = set([tuple(e) for e in l1])
        set2 = set([tuple(e) for e in l2])
        for e in l2:
            self.assertTrue(tuple(e) in set1)
        for e in l1:
            self.assertTrue(tuple(e) in set2)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Tests)
    unittest.TextTestRunner(verbosity=2).run(suite)
