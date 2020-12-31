import random

def _solution(nums, K):
    s = 0
    m = {0: -1}
    for i in range(len(nums)):
        s += nums[i]
        if (K != 0):
            s = s % K
        if s in m:
            if i - m[s] > 1:
                return True
        else:
            m[s] = i
    return False

def _generate(nums, K):
    return [nums, K, _solution(nums, K)]

class TestData():
    @staticmethod
    def basic():
        manual = [
            ([], 0, False),
            ([0, 0], 0, True),
            ([2, 3, 5], 3, False),
            ([2, 3, 5], 0, False),
            ([23, 2, 4, 6, 7],  6, True),
            ([23, 2, 6, 4, 7],  6, True)
        ]
        return manual + [ _generate(nums, K) for (nums, K) in [
                (random.sample(range(10), 5), random.randint(1,10)),
                (random.sample(range(10), 5), random.randint(1,10)),
                (random.sample(range(10), 5), random.randint(1,10)),
                (random.sample(range(10), 5), random.randint(1,10)),
                (random.sample(range(100), 50), random.randint(10,20)),
                (random.sample(range(100), 50), random.randint(10,20)),
                (random.sample(range(100), 50), random.randint(10,20)),
                (random.sample(range(100), 50), random.randint(10,20)),
                (random.sample(range(100), 50), random.randint(10,20)),
            ]
        ]

    @staticmethod
    def big():
        return [ _generate(nums, K) for (nums, K) in [
                (random.sample(range(9000), 100), random.randint(100,200)),
                (random.sample(range(9000), 100), random.randint(100,200)),
                (random.sample(range(9000), 100), random.randint(100,200)),
                (random.sample(range(9000), 1000), random.randint(1000,2000)),
                (random.sample(range(9000), 1000), random.randint(1000,2000)),
                (random.sample(range(9000), 1000), random.randint(1000,2000)),
                (random.sample(range(9000), 1000), random.randint(1000,2000)),
            ]
        ]
