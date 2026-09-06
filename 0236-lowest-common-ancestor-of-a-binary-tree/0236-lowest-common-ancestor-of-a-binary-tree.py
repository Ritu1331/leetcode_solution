# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # Base case
        if root is None:
            return None

        # If current node is p or q
        if root == p or root == q:
            return root

        # DFS on left and right
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # p and q found on different sides
        if left and right:
            return root

        # Return whichever side found p or q
        if left:
            return left

        return right
        