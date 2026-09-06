# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        # Ye function 2 cheeze return karega:
        # 1. subtree ki maximum depth
        # 2. deepest leaves ka LCA
        def dfs(root):

            if root is None: # Agar node nahi hai
                return 0, None

            left_depth, left_lca = dfs(root.left)  # Left subtree ki depth aur LCA

            right_depth, right_lca = dfs(root.right) # Right subtree ki depth aur LCA

            # Agar left subtree deeper hai
            if left_depth > right_depth:
                return left_depth + 1, left_lca

            # Agar right subtree deeper hai
            if right_depth > left_depth:
                return right_depth + 1, right_lca

            # Agar dono ki depth same hai
            # Matlab deepest leaves dono sides mein hain
            # Isliye current node hi LCA hoga
            return left_depth + 1, root

        # dfs depth aur LCA return karega
        depth, answer = dfs(root)

        # Hume sirf LCA chahiye
        return answer
        