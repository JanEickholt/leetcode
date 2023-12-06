d ef threeSum(nums):
    nums.sort()
    res = []

    for i, a in enumerate(nums):
        if a > 0:
            break
        if i > 0 and a == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            curSum = a + nums[l] + nums[r]
            if curSum > 0:
                r -= 1
            elif curSum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1

    return res
