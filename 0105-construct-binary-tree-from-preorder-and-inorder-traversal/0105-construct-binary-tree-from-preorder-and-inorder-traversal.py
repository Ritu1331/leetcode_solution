# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        self.inordermap = {}
        for i in range(len(inorder)):
            self.inordermap[inorder[i]]=i

        self.idx = 0

        def build(low , high):
            if low > high:
                return None
            
            root = TreeNode(preorder[self.idx])
            self.idx+=1

            mid = self.inordermap[root.val]

            root.left = build(low , mid-1)
            root.right = build(mid+1,high)
            return root
        
        return build(0 , len(inorder)-1)

        