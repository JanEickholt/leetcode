class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        return max([len([j for j in nums if j > 0]), len([j for j in nums if j < 0])])
