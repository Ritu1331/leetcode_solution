class Solution(object):

    def atMost(self, nums, k):

        low = 0
        count = 0
        freq = {}

        for high in range(len(nums)):

            freq[nums[high]] = freq.get(nums[high], 0) + 1

            while len(freq) > k:

                freq[nums[low]] -= 1

                if freq[nums[low]] == 0:
                    del freq[nums[low]]

                low += 1

            count += high - low + 1

        return count

    def subarraysWithKDistinct(self, nums, k):

        return self.atMost(nums, k) - self.atMost(nums, k - 1)