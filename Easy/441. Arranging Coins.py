def arrangeCoins(n):
    i = 0
    while i <= n:
        n = n - i
        i = i + 1
    return i - 1
