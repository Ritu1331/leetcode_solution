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
        # Same as:
        # Node* prev = NULL;
        self.prev = None

        # Same as:
        # Node* first = NULL;
        self.first = None

        # Same as:
        # Node* second = NULL;
        self.second = None

        def inorder(root):

            # if(root == NULL)
            if root is None:
                return

            # fun(root->left)
            inorder(root.left)

            # -------------------------
            # Process Current Node
            # -------------------------

            # if(prev == NULL)
            if self.prev is None:

                # prev = root;
                self.prev = root

            else:

                # if(root->data < prev->data)
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

                # prev = root;
                self.prev = root

            # fun(root->right)
            inorder(root.right)

        # Start Inorder Traversal
        inorder(root)

        # Swap the two wrong nodes
        self.first.val, self.second.val = self.second.val, self.first.val
        