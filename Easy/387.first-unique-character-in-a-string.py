class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {char: s.count(char) for char in s}
        for i, char in enumerate(s):
            if seen[char] == 1:
                return i
        return -1
