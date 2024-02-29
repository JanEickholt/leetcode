def minDepth(root):
    if not root:
        return 0

    if not root.left and not root.right:
        return 1

    left = minDepth(root.left) if root.left else float("inf")
    right = minDepth(root.right) if root.right else float("inf")

    return 1 + min(left, right)
