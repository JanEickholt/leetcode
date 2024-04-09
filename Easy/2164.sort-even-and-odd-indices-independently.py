class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even_nums = [num for i, num in enumerate(nums) if i % 2 == 0]
        odd_nums = [num for i, num in enumerate(nums) if i % 2 != 0]

        even_nums.sort()
        odd_nums.sort(reverse=True)

        for i, _ in enumerate(nums):
            if i % 2 == 0:
                nums[i] = even_nums.pop(0)
            else:
                nums[i] = odd_nums.pop(0)

        return nums
