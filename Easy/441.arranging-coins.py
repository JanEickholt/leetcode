class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 0
        while i <= n:
            n = n - i
            i = i + 1
        return i - 1
