class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        distance = n
        for i in range(n):
            if words[i] == target:
                forward = (i - startIndex + n) % n
                backwards = (startIndex - i + n) % n
                distance = min(distance, forward, backwards)
        return distance if distance != n else -1
