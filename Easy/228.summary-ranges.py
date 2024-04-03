# @leet start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res, last = [], []
        length = len(nums)
        for idx, val in enumerate(nums):
            if not last:
                last.append(val)
            elif val - last[-1] == 1:
                last.append(val)
            else:
                if len(last) == 1:
                    res.append(str(last[0]))
                else:
                    res.append(str(last[0]) + "->" + str(last[-1]))
                last = [val]
            if idx == length - 1:
                if len(last) == 1:
                    res.append(str(last[0]))
                else:
                    res.append(str(last[0]) + "->" + str(last[-1]))

        return res
