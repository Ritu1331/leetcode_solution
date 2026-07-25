class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_map = {}
        t_map = {}

        for i in range(len(s)):

            if s[i] in s_map and s_map[s[i]] != t[i]:
                return False

            if t[i] in t_map and t_map[t[i]] != s[i]:
                return False

            s_map[s[i]] = t[i]
            t_map[t[i]] = s[i]

        return True
        