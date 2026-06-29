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

        def dfs(root, total, diary):

            if root is None:
                return

            total += root.val
            diary.append(root.val)

            # Leaf node
            if root.left is None and root.right is None:

                if total == targetSum:
                    res.append(diary[:])   # store a copy

            else:
                dfs(root.left, total, diary)
                dfs(root.right, total, diary)

            # Backtrack
            diary.pop()

        dfs(root, 0, [])

        return res