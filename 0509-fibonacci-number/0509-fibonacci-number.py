class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n==0):
            return 0
        
        if (n==1):
            return 1
        
        ans1 = self.fib(n-1)
        ans2 = self.fib(n-2)
        return (ans1+ans2)