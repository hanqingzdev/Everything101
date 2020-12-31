"""
* https://leetcode.com/problems/word-break/
"""
def solution1(s, words):

    mem = {w:True for w in words}
    mem[''] = True
    def can_break(word):
        if word in mem:
            return mem[word]

        for prefix in words:
            if word.startswith(prefix):
                if can_break(word[len(prefix):]):
                    mem[word] = True
                    return True

        mem[word] = False
        return False

    return can_break(s)


import unittest
from unittest_data_provider import data_provider

def data():
    return [
        (True, "leetcode", ["leet", "code"]),
        (True, "applepenapple", ["apple", "pen"]),
        (False, "catsandog", ["cats", "dog", "sand", "and", "cat"]),
        (False, "abcd", ['a', 'b', 'c']),
        (True, "abcd", ['a', 'b', 'c', 'd']),
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
