def numJewelsInStones(jewels, stones):
    jewels = set(jewels)
    res = 0
    for i in stones:
        if i in jewels:
            res += 1
    return res
