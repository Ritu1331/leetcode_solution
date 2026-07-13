class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_curr = nums[0]
        min_curr = nums[0]

        max_sum = nums[0]
        min_sum = nums[0]

        for i in range(1, len(nums)):

            max_curr = max(nums[i], max_curr + nums[i])

            min_curr = min(nums[i], min_curr + nums[i])

            max_sum = max(max_sum, max_curr)

            min_sum = min(min_sum, min_curr)

        return max(max_sum, abs(min_sum))
        