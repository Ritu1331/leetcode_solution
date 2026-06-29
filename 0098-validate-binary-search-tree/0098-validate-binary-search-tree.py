# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        self.prev = None

        def inorder(node):

            if node is None:
                return True

            if not inorder(node.left):
                return False

            if self.prev and node.val <= self.prev.val:
                return False

            self.prev = node

            return inorder(node.right)

        return inorder(root)
            


        