# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.prev = None
        self.first = None
        self.second = None

        def inorder(root):
            if root is None:
                return None

            inorder(root.left)
            self.curr = root

            if self.prev is not None:
                if self.prev.val > root.val:

                    # First violation
                    if self.first is None:
                        self.first = self.prev

                    # Current node of violation
                    self.second = root

            self.prev = root

            inorder(root.right)

        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val