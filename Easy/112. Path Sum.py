def hasPathSum(root, targetSum):
    if not root:
        return False

    if not root.right and not root.left:
        return root.val == targetSum

    return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)

