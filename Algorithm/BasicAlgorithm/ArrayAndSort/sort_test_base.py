import unittest
from unittest_data_provider import data_provider
import random

class SortTest(unittest.TestCase):
    data = lambda: tuple(
        (sorted(x), x) for x in [
            [],
            [1,1],
            [1,1,1,1],
            [7,6,5,4,3,2,1],
            [1,7,5,9,7,3,4,6],
            random.sample(range(100), 10),
            random.sample(range(1000), 100)
        ]
    )

    bigData = lambda: tuple(
        (sorted(x), x) for x in [
            random.sample(range(10000), 10000),
            random.sample(range(10**9), 10**5),
            random.sample(range(10**9), 10**6)
        ]
    )
