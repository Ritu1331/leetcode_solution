class Solution(object):
    def maxSubarraySumCircular(self, nums):

        total_sum = sum(nums)

        curr_max = nums[0]
        max_sum = nums[0]

        curr_min = nums[0]
        min_sum = nums[0]

        for i in range(1, len(nums)):

            # Maximum subarray (Kadane)
            curr_max = max(nums[i], curr_max + nums[i])
            max_sum = max(max_sum, curr_max)

            # Minimum subarray
            curr_min = min(nums[i], curr_min + nums[i])
            min_sum = min(min_sum, curr_min)

        # Sab elements negative hain
        if max_sum < 0:
            return max_sum

        circular_sum = total_sum - min_sum

        return max(max_sum, circular_sum)