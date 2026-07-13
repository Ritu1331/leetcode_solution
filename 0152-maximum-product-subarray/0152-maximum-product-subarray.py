class Solution(object):
    def maxProduct(self, nums):
        curr_max = nums[0]
        curr_min = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]

            temp_max = max(n, curr_max * n, curr_min * n)
            temp_min = min(n, curr_max * n, curr_min * n)

            curr_max = temp_max
            curr_min = temp_min

            result = max(result, curr_max)

        return result