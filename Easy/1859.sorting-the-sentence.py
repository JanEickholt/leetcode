class Solution:
    def sortSentence(self, s: str) -> str:
        dic = {}
        for i in s:
            dic[i[-1]] = i[:-1]
        return ' '.join([dic[j] for j in sorted(dic)])
