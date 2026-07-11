class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        low = 0
        high = 0
        freq = {}
        res = 0
        max_freq = 0

        for high in range(len(s)):
            freq[s[high]] = freq.get(s[high] , 0)+1
            window_length = high-low+1
            max_freq = max(max_freq , freq[s[high]])

            cal = window_length - max_freq

            if (cal<=k):
                res = max(res,window_length)
            
            else:
                freq[s[low]]-=1
                low +=1
        

        return res

