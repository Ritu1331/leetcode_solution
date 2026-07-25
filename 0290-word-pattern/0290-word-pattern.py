class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()

        if len(pattern) != len(words):
            return False

        p_map = {}
        w_map = {}

        for i in range(len(pattern)):

            if pattern[i] in p_map and p_map[pattern[i]] != words[i]:
                return False

            if words[i] in w_map and w_map[words[i]] != pattern[i]:
                return False

            p_map[pattern[i]] = words[i]
            w_map[words[i]] = pattern[i]

        return True
        