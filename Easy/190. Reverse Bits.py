def reverseBits(n):
    return int(str(bin(n)[2:].zfill(32))[::-1], 2)
