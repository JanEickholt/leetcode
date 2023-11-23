def singleNumber(nums):
    digit_dict = {}
    for i in nums:
        if i in digit_dict:
            digit_dict.pop(i)
        else:
            digit_dict[i] = 1

    return digit_dict.keys()[0]
