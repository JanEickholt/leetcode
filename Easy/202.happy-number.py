class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(num) ** 2 for num in str(n))
        return n == 1