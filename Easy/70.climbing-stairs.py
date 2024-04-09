class Solution:
    def climbStairs(self, n: int) -> int:
        prev1 = 1
        prev2 = 1
        for i in range(n - 1):
            prev1, prev2 = prev2, prev1 + prev2
        return prev2
