def minimumSum(num):
    nums = "".join(sorted(str(num)))
    res = [int(nums[0] + nums[-1])]
    nums = nums[1:-1]
    res.append(int(nums[0] + nums[-1]))
    return sum(res)
