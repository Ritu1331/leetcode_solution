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
        def pathsum(root,sum):
            res = False 

            if root is None:
                res = False
                return res
        
            sum +=root.val

            if (root.left is None and root.right is None):
                if(sum == targetSum):
                    res = True
                    return res
            
            left = pathsum(root.left,sum)
            right = pathsum(root.right,sum)

        

            return left or right
        
        return pathsum(root,0)
        