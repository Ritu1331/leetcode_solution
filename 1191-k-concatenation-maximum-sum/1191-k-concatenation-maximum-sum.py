class Solution(object):

    def kadane(self, nums):

        curr = 0
        best = 0

        for num in nums:

            curr = max(0, curr + num)

            best = max(best, curr)

        return best

    def kConcatenationMaxSum(self, arr, k):

        MOD = 10**9 + 7

        if k == 1:
            return self.kadane(arr) % MOD

        total = sum(arr)

        best = self.kadane(arr + arr)

        if total > 0:

            best += (k - 2) * total

        return best % MOD