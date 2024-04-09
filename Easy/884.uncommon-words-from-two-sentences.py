class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        all_words = {}
        for word in s1.split():
            if word in all_words:
                all_words[word] += 1
            else:
                all_words[word] = 1
            for word in s2.split():
                if word in all_words:
                    all_words[word] += 1
                else:
                    all_words[word] = 1
            return [word for word in all_words if all_words[word] == 1]
