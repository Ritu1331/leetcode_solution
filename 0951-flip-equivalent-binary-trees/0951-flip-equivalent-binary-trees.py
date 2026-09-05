# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """

        if root1 is None and root2 is None:
            return True

        if root1 is None or root2 is None:
            return False

        if root1.val != root2.val:
            return False
        
        r1 = self.flipEquiv(root1.left, root2.left)
        r2 = self.flipEquiv(root1.right, root2.right)

        normal = r1 and r2

        r3 = self.flipEquiv(root1.left, root2.right)
        r4 = self.flipEquiv(root1.right, root2.left)

        flipped = r3 and r4
        return normal or flipped


        