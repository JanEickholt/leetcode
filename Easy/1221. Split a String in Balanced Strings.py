def balancedStringSplit(s):
    res = 0
    count = 0
    for char in s:
        if char == "R":
            count += 1
        else:
            count -= 1
        if count == 0:
            res += 1
    return res
