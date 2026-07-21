class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        stack = []
        
        for i in range (n):
            if not stack:
                stack.append(s[i])
                continue
            
            if(stack[-1]==s[i]):
                stack.pop()
                continue
            
            stack.append(s[i])
            
        
        return "".join(stack)



            




        