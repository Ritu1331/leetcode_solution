# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(root):

            # Empty node
            if root is None:
                return 0, 0

            # Left: height, diameter
            left_height, left_diameter = dfs(root.left)

            # Right: height, diameter
            right_height, right_diameter = dfs(root.right)

            # Current node ke through diameter
            current_diameter = left_height + right_height

            # Current subtree ki height
            height = max(left_height, right_height) + 1

            # Height aur maximum diameter return
            diameter = max(current_diameter,
                           left_diameter,
                           right_diameter)

            return height, diameter

        height, diameter = dfs(root)

        return diameter
        