class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        def backtrack(idx , temp):

            if idx==len(digits):
                res.append(temp)
                return 
            
            letters = phone[digits[idx]]

            for ch in letters:
                backtrack(idx+1 , temp + ch)
            
        backtrack(0,"")
        
        return res

