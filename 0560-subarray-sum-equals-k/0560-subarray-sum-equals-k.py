class Solution(object):
    def subarraySum(self, nums, k):

        prefix_sum = 0
        res = 0
        f = {0: 1}   # important

        for i in range(len(nums)):
            prefix_sum += nums[i]

            ques = prefix_sum - k

            if ques in f:
                res += f[ques]

            f[prefix_sum] = f.get(prefix_sum, 0) + 1

        return res
