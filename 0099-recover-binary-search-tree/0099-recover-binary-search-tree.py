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
                return

            inorder(root.left)

            if self.prev is None:
                self.prev = root

            else:
                if root.val < self.prev.val:

                    # First violation
                    if self.first is None:

                        # first = prev;
                        self.first = self.prev

                        # second = root;
                        self.second = root

                    # Second violation
                    else:

                        # second = root;
                        self.second = root

                
                self.prev = root

            inorder(root.right)
        inorder(root)

        self.first.val, self.second.val = self.second.val, self.first.val
        