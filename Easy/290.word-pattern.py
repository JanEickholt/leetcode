class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        return len({*pattern}) == len(set(s.split(" ")))
