def isPowerOfTwo(n):
    if n <= 0:
        return False

    binary = bin(n)[2:]
    return binary.count("1") == 1

