class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack =[]
        for i in range(len(s)):
            if (s[i]=='(' or s[i]=='{' or s[i]=='['):
                stack.append(s[i])
                continue 
            
            if not stack:
                return False
            
            if(stack[-1]=='(' and s[i]==')'or stack[-1]=='{' and s[i]=='}' or stack[-1]=='[' and s[i]==']'):
                stack.pop()
            else:
                return False
                
        return len(stack)==0

            
            

        