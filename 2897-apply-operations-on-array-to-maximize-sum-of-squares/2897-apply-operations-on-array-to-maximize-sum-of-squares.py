class Solution(object):
    def maxSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        bits = [0] * 32

        for x in nums:
            for bit in range(32):
                if x & (1 << bit):
                    bits[bit] += 1

        ans = 0

        for _ in range(k):
            num = 0

            for bit in range(32):
                if bits[bit] > 0:
                    num |= (1 << bit)
                    bits[bit] -= 1

            ans = (ans + num * num) % MOD

        return ans