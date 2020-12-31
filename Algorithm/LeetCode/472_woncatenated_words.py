"""
* https://leetcode.com/problems/concatenated-words/
"""

def solution1(words):
    """
    for w in words -> can we break w by rest of words? fn(w, rest_words)
        if prefix in rest_words and is prefix of w -> fn(w-prefix, rest_words - prefix)
    """

    can_break_cache = {w: True for w in words}
    def can_break(w):
        if w in can_break_cache:
            return can_break_cache[w]

        for p in words:
            if p == w:
                continue

            if w.startswith(p):
                rest_w = w[len(p):]
                can_also_break = can_break(rest_w)
                if can_also_break:
                    can_break_cache[w] = True
                    return True

        can_break_cache[w] = False
        return False

    ans = []
    for w in words:
        del can_break_cache[w]
        if can_break(w):
            ans.append(w)
        can_break_cache[w] = True

    return ans



import unittest
from unittest_data_provider import data_provider

def data():
    return [
        (
            ["catsdogcats","dogcatsdog","ratcatdogcat"],
            ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]),
    ]

class Tests(unittest.TestCase):
    @data_provider(data)
    def test_all_solutions(self, expected, *argv):
        for n in range(1, 10):
            fn_name = 'solution' + str(n)
            if fn_name in globals():
                fn = globals()[fn_name]
                #print('Testing %s with input %s' % (fn_name, str(argv)))
                ans = fn(*argv)
                self.assertEqual(len(expected), len(ans))
                self.assertEqual(set(expected), set(ans))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Tests)
    unittest.TextTestRunner(verbosity=2).run(suite)
