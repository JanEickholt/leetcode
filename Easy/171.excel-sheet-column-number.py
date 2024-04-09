class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        multiplier = 1
        for i in range(len(columnTitle) - 1, -1, -1):
            num = ord(columnTitle[i]) - 64
            result += num * multiplier
            multiplier *= 26
        return result
