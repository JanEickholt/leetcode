class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        words.sort()
        l = len(words[0]) * len(words)
        f = len(words[0])
        a = []
        ans = []
        for i in range(len(s) - l + 1):
            d = s[i:i + l]
            a = [d[j:j + f] for j in range(0, len(d), f)]
            a.sort()
            if a == words:
                ans.append(i)
        return ans
