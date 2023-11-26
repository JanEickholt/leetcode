def climbStairs(n):
    prev1, prev2 = 1, 1
    for i in range(n - 1):
        prev1, prev2 = prev2, prev1 + prev2
    return prev2
