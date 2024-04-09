class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        freq = [0] * 10000
        for num in nums:
            freq[num] += 1
            if freq[num] > 1:
                res.append(num)
        return res
