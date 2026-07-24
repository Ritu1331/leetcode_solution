class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        res = 0
        odd_found = False

        for count in freq.values():

            if count % 2 == 0:
                res += count

            else:
                res += count - 1
                odd_found = True

        if odd_found:
            res += 1

        return res