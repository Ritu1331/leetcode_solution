class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Step 1: Total sum
        total = sum(nums)

        # Step 2: Impossible cases
        if abs(target) > total:
            return 0

        if (total + target) % 2 != 0:
            return 0

        # Step 3: Positive numbers ka required sum
        required = (total + target) // 2

        # Step 4: Count Subset Sum DP
        dp = [0] * (required + 1)

        # Sum 0 banane ka 1 way: kuch bhi nahi lena
        dp[0] = 1

        # Har number ko ek baar use karna hai
        for num in nums:

            # Backward loop because 0/1 subset
            for j in range(required, num - 1, -1):

                dp[j] += dp[j - num]

        return dp[required]
        