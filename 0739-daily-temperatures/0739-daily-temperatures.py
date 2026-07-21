class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        ans = []

        for i in range(len(temperatures)-1 ,-1 ,-1):
            while stack and temperatures[stack[-1]]<=temperatures[i]:
                stack.pop()

            
            if not stack:
                ans.append(0)
            else:
                ans.append(stack[-1]-i)

            
            stack.append(i)
        ans.reverse()
        return ans
