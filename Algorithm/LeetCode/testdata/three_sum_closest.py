import random

def _solution(nums, target):
    diff = float('inf')
    nums.sort()
    for i in range(len(nums)):
        lo, hi = i + 1, len(nums) - 1
        while (lo < hi):
            sum = nums[i] + nums[lo] + nums[hi]
            if abs(target - sum) < abs(diff):
                diff = target - sum
            if sum < target:
                lo += 1
            else:
                hi -= 1
        if diff == 0:
            break
    return target - diff


def _generate(nums, target):
    return [nums, target, _solution(nums, target)]

class TestData():
    @staticmethod
    def basic():
        return [ _generate(nums, target) for (nums, target) in [
                ([-1,2,1,-4], 1), # answer is 2
                (random.sample(range(100), 3), random.randint(1, 100)),
                (random.sample(range(100), 5), random.randint(1, 100)),
                (random.sample(range(100), 5), random.randint(100, 200)),
                (random.sample(range(100), 10), random.randint(1, 100)),
                (random.sample(range(100), 10), random.randint(100, 1000)),
            ]
        ]

    @staticmethod
    def big():
        return [ _generate(nums, target) for (nums, target) in [
                (random.sample(range(9000), 100), random.randint(1, 9000)),
                (random.sample(range(9000), 100), random.randint(10000, 90000)),
                (random.sample(range(9000), 1000), random.randint(1, 9000)),
                (random.sample(range(9000), 1000), random.randint(10000, 90000)),
            ]
        ]
