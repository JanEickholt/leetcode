class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle) if needle else -1
