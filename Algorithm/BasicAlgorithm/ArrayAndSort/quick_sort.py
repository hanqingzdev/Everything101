def partition(nums, lo, hi):
    if lo >= hi:
        return lo

    pivot = nums[hi]
    biggestSmaller_i = lo - 1

    for i in range(lo, hi):
        if nums[i] < pivot:
            biggestSmaller_i += 1
            nums[biggestSmaller_i], nums[i] = nums[i], nums[biggestSmaller_i]
    biggestSmaller_i += 1
    nums[biggestSmaller_i], nums[hi] = nums[hi], nums[biggestSmaller_i]

    return biggestSmaller_i

def quickSort(nums, lo=0, hi=None):
    if hi is None:
        hi = len(nums) - 1

    if lo < hi:
        pivot_i = partition(nums, lo, hi)
        quickSort(nums, lo, pivot_i - 1)
        quickSort(nums, pivot_i + 1, hi)

    return nums
