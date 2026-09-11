# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        self.res = root.val

        def dfs(root):
            if root is None:
                return 0

            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))

            # Dono sides + current node = possible answer
            self.res = max(self.res, left + root.val + right)

            # Parent ko sirf ek side de sakte hain
            return root.val + max(left, right)

        dfs(root)
        return self.res