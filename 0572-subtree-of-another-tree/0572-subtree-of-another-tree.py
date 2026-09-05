# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        if subRoot is None:
            return True

        if root is None:
            return False

        if self.sameTree(root, subRoot):
            return True
        
        r1 = self.isSubtree(root.left, subRoot)
        r2 = self.isSubtree(root.right, subRoot)

        return r1 or r2
               
    
    def sameTree(self, root, subRoot):
        if root is None and subRoot is None:
            return True
        
        if root is None or subRoot is None:
            return False

        if root.val != subRoot.val:
            return False

        r1 = self.sameTree(root.left, subRoot.left)
        r2 = self.sameTree(root.right, subRoot.right)

        return r1 and r2





        