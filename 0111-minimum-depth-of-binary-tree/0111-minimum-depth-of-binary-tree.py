# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def dfs(root):
            if root is None:
                return 0
            
            depth_left = dfs(root.left)
            depth_right = dfs(root.right)

            if depth_left == 0:
                return depth_right + 1
            
            if depth_right == 0:
                return depth_left + 1
            
            return min(depth_left , depth_right) + 1
        return dfs(root)


'''root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Create Solution object
r = Solution()

# Call function
answer = r.minDepth(root)

print(answer)'''

        