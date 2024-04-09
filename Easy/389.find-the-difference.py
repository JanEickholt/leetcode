class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in t:
            if (not i in s) or (not s.count(i) == t.count(i)):
                return i
