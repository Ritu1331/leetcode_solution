# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        #balanced BT -> |height(left) - height(right)| <= 1

        def dfs(root):
            if root is None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            # Agar koi side unbalanced hai
            if left == -1 or right == -1:
                return -1

            # Difference 1 se zyada hai
            if abs(left - right) > 1:
                return -1

            # Height
            return max(left, right) + 1

        return dfs(root) != -1
        