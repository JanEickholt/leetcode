class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = [i for i, word in enumerate(words) if x in word]
        return res
