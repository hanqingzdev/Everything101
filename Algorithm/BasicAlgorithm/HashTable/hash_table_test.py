import unittest
from unittest_data_provider import data_provider
from hash_table import HashTable

class HashTableTest(unittest.TestCase):
    data = lambda: [
        (None, {1: 'a', 2: 'b', 1000: 'c', 1234567: 'd'}, [1,2]),
        (2, {0: 'x', 1: 'a', 2: 'b', 3: 'c', 4: 'd'}, [0,1,2,3,4])
    ]

    @data_provider(data)
    def test_simple(self, size, raw, removes):
        h = HashTable(size) if size else HashTable()

        for k, v in raw.items():
            h.put(k, v)

        self.assertEqual(len(raw), h.size)
        for k, v in raw.items():
            self.assertEqual(v, h.get(k))

        for k in removes:
            h.remove(k)
            del raw[k]
            self.assertEqual(len(raw), h.size)
            self.assertEqual(raw.get(k), h.get(k))

if __name__ == '__main__':
    unittest.main()
