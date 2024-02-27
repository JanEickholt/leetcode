def firstMissingPositive(nums):
    res = 1
    nums = set(nums)
    while res in nums:
        res += 1
    return res
