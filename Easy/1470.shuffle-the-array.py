class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        buffer = [[] for i in range(n)]
        for idx, val in enumerate(nums):
            buffer[idx % n].append(val)
        return [val for sublist in buffer for val in sublist]
