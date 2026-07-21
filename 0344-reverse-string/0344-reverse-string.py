class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        stack = []

        # Push all elements
        for char in s:
            stack.append(char)

        # Pop and put back into s
        i = 0
        while stack:
            s[i] = stack.pop()
            i += 1