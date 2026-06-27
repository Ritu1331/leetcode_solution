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
        self.ans = None
        def dfs(node):
            if node is None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            if node == p or node == q:
                self_node = 1
            else:
                self_node = 0
            
            total = left + right + self_node

            if total == 2 and self.ans is None:
                self.ans = node

            return total

        dfs(root)

        return self.ans



        