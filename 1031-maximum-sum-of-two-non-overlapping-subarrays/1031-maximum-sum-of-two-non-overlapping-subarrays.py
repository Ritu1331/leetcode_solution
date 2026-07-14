class Solution(object):

    def helper(self, nums, L, M):

        n = len(nums)

        # Prefix sum
        prefix = [0] * (n + 1 )

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # Sum of first L elements
        maxL = prefix[L] - prefix[0]

        ans = 0

        for i in range(L + M, n + 1):

            # Best L-length subarray before current M
            left_sum = prefix[i - M] - prefix[i - M - L]

            maxL = max(maxL, left_sum)

            # Current M-length subarray
            currM = prefix[i] - prefix[i - M]

            ans = max(ans, maxL + currM)

        return ans

    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):

        return max(
            self.helper(nums, firstLen, secondLen),
            self.helper(nums, secondLen, firstLen)
        )