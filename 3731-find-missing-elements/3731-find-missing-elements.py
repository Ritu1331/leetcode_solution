class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = set(nums)

        minimum = min(nums)
        maximum = max(nums)

        ans = []

        for num in range(minimum, maximum + 1):

            if num not in seen:
                ans.append(num)

        return ans