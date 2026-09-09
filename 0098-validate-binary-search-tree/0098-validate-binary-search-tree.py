# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    def isValidBST(self, root):

        self.prev = None
        self.ans = True

        def inorder(root):

            if root is None:
                return

            # Step 1 : Visit left subtree
            inorder(root.left)

            # Step 2 : Process current node
            if self.prev is None:
                self.prev = root
            else:

                if root.val <= self.prev.val:
                    self.ans = False

                self.prev = root

            # Step 3 : Visit right subtree
            inorder(root.right)   # tc = n , sc = h

        inorder(root)

        return self.ans

        '''arr = []

def inorder(root):
    if root is None:
        return

    inorder(root.left)
    arr.append(root.val)
    inorder(root.right)

inorder(root)

for i in range(1, len(arr)):    # tc = n , sc -- n
    if arr[i] <= arr[i - 1]:
        return False

return True'''