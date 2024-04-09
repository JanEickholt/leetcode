import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = re.findall(r'([0-9A-Za-z]+)', s)
        stripped = ''.join(stripped)
        stripped = stripped.lower()
        return stripped == stripped[::-1]
