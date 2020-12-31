"""
# Problem Statement
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

* https://leetcode.com/problems/combination-sum-ii/

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [ [1,1,6], [1,2,5], [1,7], [2,6] ]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: [ [1,2,2], [5] ]

Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
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
        if target > 0 -> for each n in candidates, result is [n] + fn(restOfCandidates, target - n)
    """
    def fn(candidates, target):
        allSum = sum(candidates)
        if allSum < target:
            return []
        elif allSum == target:
            return [candidates]

        ans = set()
        for i in range(len(candidates)):
            n = candidates[i]
            rest = candidates[:i] + candidates[i+1:]
            newTarget = target - n

            if newTarget == 0:
                ans.add(tuple([n]))
                continue
            elif newTarget < 0:
                continue
            else:
                restAns = fn(rest, target - n)
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
    same idea as solution1, remove numbers bigger than target ealier
    """
    candidates.sort()

    def fn(candidates, target):
        ans = set()
        allSum = sum(candidates)
        if allSum < target:
            return []
        elif allSum == target:
            return [candidates]

        for i in range(len(candidates)):
            n = candidates[i]

            newCandidates = candidates[i+1:]
            newTarget = target - n

            if newTarget > 0:
                newAnses = fn(newCandidates, newTarget)
                for e in newAnses:
                    ans.add(tuple([n] + list(e)))
            elif newTarget == 0:
                ans.add(tuple([n]))
                break
            else: # newTarget < 0
                break
        return ans

    tupleAns = fn(candidates, target)
    ans = [list(t) for t in tupleAns]
    return ans

import unittest
from unittest_data_provider import data_provider

def data():
    return [
        ([2,5,2,1,2], 5, [[1,2,2], [5]]),
        ([10,1,2,7,6,1,5], 8, [[1,1,6], [1,2,5], [1,7], [2,6]]),
        ([1], 1, [[1]]),
        ([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 30, []),
        ([1,2,3,4,5,6,7,8,9,10], 19,
            [[1,2,3,4,9],[1,2,3,5,8],[1,2,3,6,7],[1,2,4,5,7],[1,2,6,10],[1,2,7,9],[1,3,4,5,6],[1,3,5,10],[1,3,6,9],[1,3,7,8],[1,4,5,9],[1,4,6,8],[1,5,6,7],[1,8,10],[2,3,4,10],[2,3,5,9],[2,3,6,8],[2,4,5,8],[2,4,6,7],[2,7,10],[2,8,9],[3,4,5,7],[3,6,10],[3,7,9],[4,5,10],[4,6,9],[4,7,8],[5,6,8],[9,10]]),
    ]

class Tests(unittest.TestCase):
    @data_provider(data)
    def test_solution1(self, nums, target, expected):
        self.assertListIdentical(expected, solution1(nums, target))

    @data_provider(data)
    def test_solution2(self, nums, target, expected):
        self.assertListIdentical(expected, solution2(nums, target))

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
