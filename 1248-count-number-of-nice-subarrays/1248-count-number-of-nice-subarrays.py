class Solution(object):

    def atMost(self, nums, k):

        low = 0
        count = 0
        odd_count = 0

        for high in range(len(nums)):

            # Count odd numbers
            if nums[high] % 2 == 1:
                odd_count += 1

            # Shrink window
            while odd_count > k:

                if nums[low] % 2 == 1:
                    odd_count -= 1

                low += 1

            # Number of valid subarrays ending at high
            count += high - low + 1

        return count

    def numberOfSubarrays(self, nums, k):

        return self.atMost(nums, k) - self.atMost(nums, k - 1)