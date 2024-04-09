class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = float('inf')
        for i in range(len(nums) - 2):
            a, b = i + 1, len(nums) - 1
            while a < b:
                if nums[i] + nums[a] + nums[b] == target:
                    return nums[i] + nums[a] + nums[b]
                else:
                    if abs((nums[i] + nums[a] + nums[b]) - target) < abs(closest - target):
                        closest = nums[i] + nums[a] + nums[b]
                    if nums[i] + nums[a] + nums[b] > target:
                        b -= 1
                    else:
                        a += 1
        return closest
