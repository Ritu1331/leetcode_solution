class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        freq = {}
        left = []
        middle = ""

        for ch in s:
            freq[ch] = freq.get(ch , 0) + 1
        
        for ch in sorted(freq):
            left.append(ch * (freq[ch] // 2))
                
            
            if (freq[ch] % 2 == 1):
                middle = ch
            
        
        left = "".join(left)
        return left + middle + left[::-1]

        

        