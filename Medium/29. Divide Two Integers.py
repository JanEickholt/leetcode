def divide(dividend, divisor):
    if dividend == -2147483648 and divisor == -1:
        return 2147483647
    if dividend == 0:
        return 0
    if divisor == 1:
        return dividend
    if divisor == -1:
        return -dividend
    sign = 1
    if dividend < 0:
        sign = -sign
        dividend = -dividend
    if divisor < 0:
        sign = -sign
        divisor = -divisor
    res = 0
    while dividend >= divisor:
        tmp = divisor
        i = 1
        while dividend >= tmp:
            dividend -= tmp
            res += i
            i <<= 1
            tmp <<= 1
    return res * sign
