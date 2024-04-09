class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = ''.join(c.lower() if c.isalpha() else ' ' for c in paragraph).split()
        word_count = {word: words.count(word) for word in set(words) if word not in banned}
        return max(word_count, key=word_count.get)
