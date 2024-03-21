def countPrimeSetBits(left, right):
    return sum(
        1
        for i in range(left, right + 1)
        if bin(i).count("1") in {2, 3, 5, 7, 11, 13, 17, 19}
    )
