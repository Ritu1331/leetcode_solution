class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        count = 0
        valid = ""

        for ch in s:
            if ch == "(":
                count += 1
                valid += "("
            
            if ch == ")":
                count  -= 1
                valid += ")"
            
            if count == 0 :
                
                valid = valid[1:len(valid)-1]
                ans += valid
                valid = ""
        
        return ans
                    