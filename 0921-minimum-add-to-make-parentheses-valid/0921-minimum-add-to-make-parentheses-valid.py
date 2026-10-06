class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        balance = 0 
        ans = 0
        for ch in s:
            if ch == "(":
                balance += 1
            
            else:  # ')'
                if balance > 0:
                    balance -= 1
                else:
                    ans += 1

        return balance + ans 
        
        """ans     → missing '('
balance → missing ')'"""
            