import random

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def _solution(nums):
    is_odd = 1
    odd = []
    even = []
    for n in nums:
        if is_odd == 1:
            odd.append(n)
        else:
            even.append(n)
        is_odd = is_odd * -1
    return _convertArrayToLinked(odd + even)


def _convertArrayToLinked(nums):
    dummy_head = ListNode()
    curr = dummy_head

    for n in nums:
        curr.next = ListNode(n)
        curr = curr.next
    return dummy_head.next

def _generate(nums):
    return [_convertArrayToLinked(nums), _solution(nums)]

class TestData():
    @staticmethod
    def basic():
        return [ _generate(nums) for nums in [
                [],
                [1],
                [1,2],
                [1,2,3,4,5],
                [1,2,3,4,5,6],
                random.sample(range(100), 3),
                random.sample(range(100), 5),
                random.sample(range(100), 5),
                random.sample(range(100), 10),
                random.sample(range(100), 10),
            ]
        ]

    @staticmethod
    def big():
        return [ _generate(nums) for nums in [
                random.sample(range(9000), 100),
                random.sample(range(9000), 100),
                random.sample(range(9000), 1000),
                random.sample(range(9000), 1000),
                random.sample(range(9000), 1000),
            ]
        ]
