class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        return ''.join(sorted(zip(indices, s), key=lambda x: x[0]))
