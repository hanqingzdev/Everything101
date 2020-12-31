def merge(nums1, nums2):
    l1, l2 = len(nums1), len(nums2)
    if l1 == 0 and l2 == 0:
        return []
    elif l1 == 0 and l2 > 0:
        return nums2
    elif l1 > 0 and l2 == 0:
        return nums1
    else: # both
        i1, i2 = 0, 0
        merged = []
        while i1 < l1 and i2 < l2:
            if nums1[i1] < nums2[i2]:
                merged.append(nums1[i1])
                i1 += 1
            else:
                merged.append(nums2[i2])
                i2 += 1

        if i1 < l1:
            merged.extend(nums1[i1:])
        elif i2 < l2:
            merged.extend(nums2[i2:])

        return merged

def mergeSort(nums):
    l = len(nums)
    if l <= 1:
        return nums
    #elif l == 2:
    #    return nums if nums[0] <= nums[1] else nums[::-1]
    else:
        mid = l // 2
        left = mergeSort(nums[:mid])
        right = mergeSort(nums[mid:])

        return merge(left, right)
