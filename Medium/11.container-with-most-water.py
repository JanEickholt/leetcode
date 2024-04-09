class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_width = 0
        max_height = max(height)
        left = 0
        right = len(height)-1
        while left < right:
            width = min(height[left], height[right]) * (right - left)
            max_width = max(width, max_width)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            if max_height * (right - left) <= max_width:
                break
        return max_width
