def numberGame(nums):
    nums.sort()

    for i in range(0, len(nums), 2):
        if i + 1 < len(nums):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]

    return nums

