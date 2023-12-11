def sortedArrayToBST(nums):
    if len(nums) == 0:
        return None
    m = len(nums) // 2
    n = TreeNode(nums[m])
    n.left = sortedArrayToBST(nums[:m])
    n.right = sortedArrayToBST(nums[m + 1:])
    return n
