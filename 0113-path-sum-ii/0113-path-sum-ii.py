# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        res = []

        def dfs(root, path, target):

            if root is None:
                return
            
            path.append(root.val)

            target = target- root.val
            if root.left is None and root.right is None:
                if target == 0:
                    res.append(path[:])


            dfs(root.left, path, target)
            dfs(root.right, path, target)
        
            path.pop()

        dfs(root, [], targetSum)
            
        return res
        
        