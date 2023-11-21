def isPowerOfTwo(n):
    if n <= 0:
        return False

    binary = bin(n)[2:]
    return binary.count("1") == 1


def isPowerOfTwo(n):
    return n > 0 and not n & (n - 1)
