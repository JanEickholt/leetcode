class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1]
        a = b = c = 0
        for _ in range(n - 1):
            res.append(min(res[a] * 2, res[b] * 3, res[c] * 5))
            if res[-1] == res[a] * 2:
                a += 1
            if res[-1] == res[b] * 3:
                b += 1
            if res[-1] == res[c] * 5:
                c += 1
        return res[-1]
