class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        k = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < target:
                    k += 1
                    j += 1
                i += 1
            return k
