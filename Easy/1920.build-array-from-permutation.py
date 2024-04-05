class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res = [0 for _ in range(len(nums))]
        for idx, i in enumerate(nums):
            res[idx] = nums[i]

        return res
