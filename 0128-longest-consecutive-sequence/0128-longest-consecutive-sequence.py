class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        res = 0

        for num in s:
            count = 0
            if num - 1 not in s:
                curr = num
                count += 1
                while curr + 1 in s:
                    count += 1
                    curr += 1
                res = max(res,count)
        

        return res
        