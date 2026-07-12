from collections import Counter

class Solution(object):
    def checkInclusion(self, s1, s2):
        
        if len(s1) > len(s2):
            return False

        need = {}
        window = {}

        for ch in s1:
            need[ch] = need.get(ch,0) + 1
        
        left = 0
        for right in range(len(s2)):

            window[s2[right]] = window.get(s2[right] , 0) + 1

            window_size = right - left + 1
            if window_size  > len(s1):
                window[s2[left]] -= 1
                
                if window[s2[left]] == 0:
                    del window[s2[left]]
                
                left += 1


            if window == need:
                return True
        

        return False

        