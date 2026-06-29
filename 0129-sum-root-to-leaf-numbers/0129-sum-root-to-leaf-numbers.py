# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def rootsum(root, total):

            if root is None:
                return 0

            total = total * 10 + root.val

            # Leaf node
            if root.left is None and root.right is None:
                return total

            left = rootsum(root.left, total)
            right = rootsum(root.right, total)

            return left + right

        return rootsum(root, 0)