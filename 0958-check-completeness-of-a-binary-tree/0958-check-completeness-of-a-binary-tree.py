# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return True

        q = deque([root])
        null_found = False

        while q:

            node = q.popleft()

            if node is None:
                null_found = True

            else:

                if null_found:
                    return False

                q.append(node.left)
                q.append(node.right)

        return True
        