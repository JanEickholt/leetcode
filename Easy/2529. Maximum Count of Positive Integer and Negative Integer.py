def maximumCount(nums):
    return max([len([j for j in nums if j > 0]), len([j for j in nums if j < 0])])
