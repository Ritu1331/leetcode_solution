# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
       # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        if root is None:
            return []

        q = deque()
        ans = []
        
        q.append(root)
        lefttoright = True
        while q:
            temp = []
            levelsize = len(q)

            for i in range(levelsize):
                node = q.popleft()
                temp.append(node.val)

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
                
            if not lefttoright:
                temp.reverse()

            
            ans.append(temp)

            lefttoright = not lefttoright
        return ans
        
        