def minPartitions(n):
    for digit in range(9, 0, -1):
        if str(digit) in n:
            return digit
    return 0
