class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        s2 = s[1:] + s[:-1]
        return s in s2
