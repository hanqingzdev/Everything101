"""
* https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),

Example 1:
Input: s = "babad" Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd" Output: "bb"

Example 3:
Input: s = "a" Output: "a"

Example 4:
Input: s = "ac" Output: "a"
"""

def solution1(s):
    l = len(s)

    def expand(i1, i2):
        lo, hi = i1, i2

        while lo >= 0 and hi < l and s[lo] == s [hi]:
            lo -= 1
            hi += 1
        return (lo + 1, hi - 1)

    max_size = 0
    max_pos = (-1, -1)
    for i in range(l):
        for (lo, hi) in [ expand(i, i), expand(i - 1, i) ]:
            if hi - lo + 1 > max_size:
                max_size = hi - lo + 1
                max_pos = (lo, hi)

    return s[max_pos[0]:max_pos[1]+1] if max_size > 0 else ''


import unittest
from unittest_data_provider import data_provider

def data():
    #output, nums
    return [
        ('bab', 'babad'),
        ('bb', 'cbbd'),
        ('a', 'ac'),
        ('aaaaa', 'baaaaad'),
        ('bcdcdcb', 'abcdcdcbbb'),
    ]

class Tests(unittest.TestCase):
    @data_provider(data)
    def test_solution1(self, expected, *argv):
        self.assertEqual(expected, solution1(*argv))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Tests)
    unittest.TextTestRunner(verbosity=2).run(suite)
