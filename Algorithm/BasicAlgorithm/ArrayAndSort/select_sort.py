def selectSort(nums):
    l = len(nums)
    for i in range(l):
        for j in range(i + 1, l):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums
