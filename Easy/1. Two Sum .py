def twoSum(nums, target):
    dic = {}
    for idx, num in enumerate(nums):
        if target - num in dic:
            return [dic[target - num], idx]
        dic[num] = idx
    return []