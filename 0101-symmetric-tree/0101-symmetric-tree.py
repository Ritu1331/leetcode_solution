# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return True

        def mirror (p,q):
            if p is None and q is None:
                return True
        
            if p is None or q is None:
                return False
        
            if p.val!=q.val:
                return False
        
            r1 = mirror(p.left , q.right)
            r2 = mirror(p.right , q.left)

            return r1 and r2

        return mirror(root.left, root.right)

        

        

        