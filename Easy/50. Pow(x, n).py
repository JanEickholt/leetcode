def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    if n < 0:
        return 1 / myPow(x, -n)
    if n == 0:
        return 1
    if n % 2 == 0:
        return myPow(x * x, n // 2)
    else:
        return x * myPow(x * x, (n - 1) // 2)