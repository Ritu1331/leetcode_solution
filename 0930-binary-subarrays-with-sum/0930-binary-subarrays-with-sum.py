class Solution(object):

    def atMost(self, nums, goal):

        if goal < 0:
            return 0

        low = 0
        total = 0
        count = 0

        for high in range(len(nums)):

            total += nums[high]

            while total > goal:

                total -= nums[low]
                low += 1

            count += high - low + 1

        return count

    def numSubarraysWithSum(self, nums, goal):

        return self.atMost(nums, goal) - self.atMost(nums, goal - 1)