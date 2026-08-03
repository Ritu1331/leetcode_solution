class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        '''s = str(x)

        i = 0
        j = len(s) - 1    ### tc and sc = o(n)

        while i < j:
            if s[i] != s[j]:
                return False

            i += 1
            j -= 1

        return True'''

        if x < 0 or( x % 10 == 0 and x != 0):
            return False
        
        reverse = 0

        while x > reverse:
            digit = x % 10
            reverse = reverse * 10 + digit
            x = x // 10

        if x == reverse or x == reverse // 10:
            return True 
        
        return False 



    
        
        