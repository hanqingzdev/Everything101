"""
# Problem Statement
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers
sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two
combinations are unique if the frequency of at least one of the chosen numbers
is different.

It is guaranteed that the number of unique combinations that sum up to target is
less than 150 combinations for the given input.

* https://leetcode.com/problems/combination-sum/

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation: 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.  These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []

Example 4:
Input: candidates = [1], target = 1
Output: [[1]]

Example 5:
Input: candidates = [1], target = 2
Output: [[1,1]]

## Constraints:
1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500
"""

"""
:type candidates: List[int]
:type target: int
:rtype: List[List[int]]
"""

def solution1(candidates, target):
    """
    fn(candidates, target)
        if target < 0 -> None
        if target == 0 -> []
        if target > 0 -> for each n in candidates, result is [n] + fn(candidate, target - n)
    """
    def fn(candidates, target):
        allSum = sum(candidates)

        ans = set()
        for n in candidates:
            newTarget = target - n

            if newTarget == 0:
                ans.add(tuple([n]))
                continue
            elif newTarget < 0:
                continue
            else:
                restAns = fn(candidates, target - n)
                for oneRestAns in restAns:
                    ans.add(tuple(sorted([n] + list(oneRestAns))))
        return ans

    ansSet = fn(candidates, target)
    ans = []
    for e in ansSet:
        ans.append(list(e))

    return ans

def solution2(candidates, target):
    """
    candidates.sort()
    same idea as solution2, remove numbers bigger than target ealier
    """
    candidates.sort()

    def fn(candidates, target):
        ans = set()

        for n in candidates:
            newTarget = target - n

            if newTarget > 0:
                newAnses = fn(candidates, newTarget)
                for e in newAnses:
                    ans.add(tuple(sorted([n] + list(e))))
            elif newTarget == 0:
                ans.add(tuple([n]))
                break
            else: # newTarget < 0
                break
        return ans

    tupleAns = fn(candidates, target)
    ans = [list(t) for t in tupleAns]
    return ans

def solution3(candidates, target):
    # DP
    dp = {} # (i, k) -> [all combinations to k with candidate[i] in it]
    # dp[(i, k)] = dp[j, k-candidates[i]] + c[i] for j in (0->len(candidates))
    # summ all dp[(i, target)]

    l = len(candidates)
    for i in range(l):
        dp[(i, 0)] = [[]]

    for k in range(1, target + 1):
        for i in range(l):
            n = candidates[i]
            newK = k - n
            if newK < 0:
                dp[(i, k)] = []
            elif newK == 0:
                dp[(i, k)] = [[n]]
            else: # newK > 0:
                if (i, k) not in dp:
                    dp[(i, k)] = []
                for j in range(l):
                    subAns = dp[j, newK]
                    for e in subAns:
                        dp[i, k].append([n] + e)
    ans = set()
    for i in range(l):
        for e in dp[(i, target)]:
            ans.add(tuple(sorted(e)))
    return [list(e) for e in ans]


import unittest
from unittest_data_provider import data_provider

def data():
    return [
        ([2,3,6,7], 7, [[2,2,3],[7]]),
        ([2,3,5], 8, [[2,2,2,2],[2,3,3],[3,5]]),
        ([2], 1, []),
        ([1], 1, [[1]]),
        ([1], 2, [[1,1]]),
        ([4,8,11,10,9,3,12,7,6], 25,
            [[3,3,3,3,3,3,3,4],[3,3,3,3,3,3,7],[3,3,3,3,3,4,6],[3,3,3,3,3,10],[3,3,3,3,4,9],[3,3,3,3,6,7],[3,3,3,4,4,4,4],[3,3,3,4,4,8],[3,3,3,4,6,6],[3,3,3,4,12],[3,3,3,6,10],[3,3,3,7,9],[3,3,3,8,8],[3,3,4,4,4,7],[3,3,4,4,11],[3,3,4,6,9],[3,3,4,7,8],[3,3,6,6,7],[3,3,7,12],[3,3,8,11],[3,3,9,10],[3,4,4,4,4,6],[3,4,4,4,10],[3,4,4,6,8],[3,4,4,7,7],[3,4,6,6,6],[3,4,6,12],[3,4,7,11],[3,4,8,10],[3,4,9,9],[3,6,6,10],[3,6,7,9],[3,6,8,8],[3,7,7,8],[3,10,12],[3,11,11],[4,4,4,4,9],[4,4,4,6,7],[4,4,6,11],[4,4,7,10],[4,4,8,9],[4,6,6,9],[4,6,7,8],[4,7,7,7],[4,9,12],[4,10,11],[6,6,6,7],[6,7,12],[6,8,11],[6,9,10],[7,7,11],[7,8,10],[7,9,9],[8,8,9]]),
    ]

class Tests(unittest.TestCase):
    @data_provider(data)
    def test_solution1(self, nums, target, expected):
        self.assertListIdentical(expected, solution1(nums, target))

    @data_provider(data)
    def test_solution2(self, nums, target, expected):
        self.assertListIdentical(expected, solution2(nums, target))

    @data_provider(data)
    def test_solution3(self, nums, target, expected):
        self.assertListIdentical(expected, solution3(nums, target))

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
