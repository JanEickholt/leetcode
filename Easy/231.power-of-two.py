class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        binary = bin(n)[2:]
        return binary.count("1") == 1


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not n & (n - 1)
