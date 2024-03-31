class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factor = 1
        if k == 1:
            return 1

        for i in range(2, n + 1):
            if n % i == 0:
                factor += 1
            if factor == k:
                return i
        return -1
