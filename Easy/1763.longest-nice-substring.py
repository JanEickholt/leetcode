class Solution:
    def isNice(self, s: str) -> bool:
        if len(s) < 2:
            return False
        for i in s:
            if i.isupper():
                if i.lower() not in s:
                    return False
            else:
                if i.upper() not in s:
                    return False
        return True

    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
        res = ""
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if self.isNice(s[i:j+1]):
                    if len(res) < len(s[i:j + 1]):
                        res = s[i:j + 1]
        return res
