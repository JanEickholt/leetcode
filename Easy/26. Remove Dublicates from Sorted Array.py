def removeDuplicates(nums):
    if not nums:
        return 0

    number = nums[0]
    i = 0
    while i < len(nums)-1:
        if number == nums[i+1]:
            nums.pop(i+1)
            continue
        i+=1
        number = nums[i]

    print(nums)
    return len(nums)

