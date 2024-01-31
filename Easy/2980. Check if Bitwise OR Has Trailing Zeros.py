
def hasTrailingZeros(nums):
    return len([n for n in nums if n % 2 == 0]) >= 2