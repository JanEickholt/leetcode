class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        sorted_nums = [0] * len(nums)
        even_index = 0
        odd_index = 1

        for num in nums:
            if num % 2 == 0:
                sorted_nums[even_index] = num
                even_index += 2
            else:
                sorted_nums[odd_index] = num
                odd_index += 2

        return sorted_nums
