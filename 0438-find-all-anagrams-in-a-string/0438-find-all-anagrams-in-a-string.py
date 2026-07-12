
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        need = {}
        window = {}
        res = []

        for ch in p:
            need[ch] = need.get(ch , 0) + 1

        left = 0
        for right in range(len(s)):
            window[s[right]] = window.get(s[right] , 0) + 1

            if (right - left + 1) > len(p):
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                
                left += 1
                

            if window == need:
                res.append(left)
        
        return res