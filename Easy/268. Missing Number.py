def missingNumber(nums):
    return (list(set(range(0,len(nums)+1)) - set(nums)) or [0])[0]

