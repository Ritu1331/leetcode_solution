class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []

        for ch in s:
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1

                if stack[-1][1] == k:
                    stack.pop()
            
            else:
                stack.append([ch,1])
        

        ans = ""

        for ch , count in stack:
            ans = ans + ch * count
        
        return ans 

            