class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        missing = set([x for x in range(1, len(nums) + 1)])
        for i in nums:
            if i in missing:
                missing.remove(i)
        return missing
