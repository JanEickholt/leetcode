class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = {}
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        for i in t:
            if i not in freq:
                return False
            if freq[i] == 0:
                return False
            else:
                freq[i] -= 1

        return True
