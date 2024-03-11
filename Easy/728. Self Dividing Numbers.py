def selfDividingNumbers(left, right):
    res = []
    for num in range(left, right + 1):
        for char in str(num):
            if char == "0":
                break
            if num % int(char) != 0:
                break
        else:
            res.append(num)

    return res
