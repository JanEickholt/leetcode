class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
            elif zero_count > 0:
                nums[i], nums[i - zero_count] = 0, nums[i]
