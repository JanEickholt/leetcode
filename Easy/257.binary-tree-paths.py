class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        result = []
        stack = [(root, str(root.val))]

        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                result.append(path)
            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))

        return result