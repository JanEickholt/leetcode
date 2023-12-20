def getCommon(nums1, nums2):
    nums1 = set(nums1)
    nums2 = set(nums2)
    res = nums1 & nums2
    if res:
        return min(res)
    else:
        return -1
