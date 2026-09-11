# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if root is None :
            return False
        
        targetSum = targetSum - root.val

        if root.left is None and root.right is None:
            return targetSum == 0 #true else False

        R1 = self.hasPathSum(root.left, targetSum)
        R2 = self.hasPathSum(root.right, targetSum)

        return R1 or R2
        