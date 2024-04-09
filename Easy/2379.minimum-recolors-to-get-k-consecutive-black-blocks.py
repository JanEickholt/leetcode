class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        return min(sum(b == 'W' for b in blocks[i:i + k]) for i in range(len(blocks) - k + 1))
