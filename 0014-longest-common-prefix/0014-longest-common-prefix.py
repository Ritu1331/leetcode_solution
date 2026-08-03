class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        prefix = strs[0]

        for word in strs[1:]:

            while word[:len(prefix)] != prefix:
                prefix = prefix[:-1]

                if prefix == "":
                    return ""

        return prefix
        