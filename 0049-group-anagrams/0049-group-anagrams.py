class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group = {}

        for word in strs:
            key = ''.join(sorted(word))

            if key not in group:
                group[key] = []
            
            group[key].append(word)

        return list(group.values())


        