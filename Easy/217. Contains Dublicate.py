# slow but elegant solution
def containsDuplicate(nums):
    return len(set(nums)) != len(nums)


# Faster but less elegant solution
def containsDuplicate(nums):
    seen = {}
    for i in nums:
        if i in seen:
            return True
        else:
            seen[i] = True

    return False