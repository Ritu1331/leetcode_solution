# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """

        if not root:
            return False

        # Stack for inorder iterator (smallest -> largest)
        asc = []

        # Stack for reverse inorder iterator (largest -> smallest)
        desc = []

        # Push all left nodes
        node = root
        while node:
            asc.append(node)
            node = node.left

        # Push all right nodes
        node = root
        while node:
            desc.append(node)
            node = node.right

        # -------- getSmall() --------
        def getSmall():
            if not asc:
                return None

            small = asc.pop()

            node = small.right
            while node:
                asc.append(node)
                node = node.left

            return small

        # -------- getBig() --------
        def getBig():
            if not desc:
                return None

            big = desc.pop()

            node = big.left
            while node:
                desc.append(node)
                node = node.right

            return big

        left = getSmall()
        right = getBig()

        while left != right:

            total = left.val + right.val

            if total == k:
                return True

            elif total < k:
                left = getSmall()

            else:
                right = getBig()

        return False