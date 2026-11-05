
class Solution:
    def isInterleave(self, s1, s2, s3):

        m, n = len(s1), len(s2)

        # Length check
        if m + n != len(s3):
            return False

        # DP table
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = True

        for i in range(m + 1):
            for j in range(n + 1):

                # Take character from s1
                if i > 0 and s1[i-1] == s3[i+j-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j]

                # Take character from s2
                if j > 0 and s2[j-1] == s3[i+j-1]:
                    dp[i][j] = dp[i][j] or dp[i][j-1]

        return dp[m][n]
