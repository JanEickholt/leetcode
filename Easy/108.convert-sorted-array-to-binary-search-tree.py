class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        m = len(nums) // 2
        n = TreeNode(nums[m])
        n.left = self.sortedArrayToBST(nums[:m])
        n.right = self.sortedArrayToBST(nums[m + 1:])
        return n
