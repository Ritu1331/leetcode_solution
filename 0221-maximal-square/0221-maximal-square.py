class Solution(object):
    def maximalSquare(self, matrix):

        m = len(matrix)
        n = len(matrix[0])

        dp = [[0] * n for _ in range(m)]

        max_side = 0

        for i in range(m):
            for j in range(n):

                if matrix[i][j] == "1":

                    if i == 0 or j == 0:
                        dp[i][j] = 1

                    else:
                        dp[i][j] = 1 + min(
                            dp[i-1][j],      # top
                            dp[i][j-1],      # left
                            dp[i-1][j-1]     # diagonal
                        )

                    max_side = max(max_side, dp[i][j])

        return max_side * max_side