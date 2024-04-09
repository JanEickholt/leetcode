class Solution:
    def generateParenthesis(self, n: int, cnt=0) -> List[str]:
        if n > 0 <= cnt:
            return ['(' + p for p in self.generateParenthesis(n - 1, cnt + 1)] + \
                [')' + p for p in self.generateParenthesis(n, cnt - 1)]
        return [')' * cnt] * (not n)
