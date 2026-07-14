class Solution(object):

    def helper(self, nums, L, M):

        # Create prefix sum in the same array
        prefix = nums[:]

        for i in range(1, len(prefix)):
            prefix[i] += prefix[i - 1]

        # Function to get subarray sum
        def get_sum(left, right):

            if left == 0:
                return prefix[right]

            return prefix[right] - prefix[left - 1]

        maxL = get_sum(0, L - 1)

        ans = 0

        for end in range(L + M - 1, len(nums)):

            # Sum of the latest L-sized subarray before M
            left_sum = get_sum(end - M - L + 1, end - M)

            maxL = max(maxL, left_sum)

            # Current M-sized subarray
            currM = get_sum(end - M + 1, end)

            ans = max(ans, maxL + currM)

        return ans

    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):

        return max(
            self.helper(nums, firstLen, secondLen),
            self.helper(nums, secondLen, firstLen)
        )


r = Solution()

nums = [0, 6, 5, 2, 2, 5, 1, 9, 4]

print(r.maxSumTwoNoOverlap(nums, 1, 2))