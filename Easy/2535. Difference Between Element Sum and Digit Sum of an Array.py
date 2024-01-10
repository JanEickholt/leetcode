def differenceOfSum(nums):
    elem_sum = sum(nums)
    digit_sum = sum(int(digit) for num in nums for digit in str(num))
    return abs(elem_sum - digit_sum)
