class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        copy = [0 for _ in range(len(nums))]
        smallest = len(nums) - nums.index(min(nums))
        for idx, val in enumerate(nums):
            copy[(idx + smallest) % (len(nums))] = val

        if copy == sorted(copy):
            return smallest % len(nums)

        return -1
