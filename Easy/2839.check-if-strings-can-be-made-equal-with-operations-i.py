class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if i < 2:
                    if s1[i] != s2[i + 2]:
                        return False
                else:
                    if s1[i] != s2[i - 2]:
                        return False

        return True
