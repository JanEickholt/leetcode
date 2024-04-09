class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSame(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return isSame(node1.left, node2.right) and isSame(node1.right, node2.left)

        return isSame(root, root)
