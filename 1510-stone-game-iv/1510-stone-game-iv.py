class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dp = [False] * (n + 1)

        for i in range(1, n + 1):

            j = 1

            while j * j <= i:

                square = j * j

                if dp[i - square] == False:
                    dp[i] = True
                    break

                j += 1

        return dp[n]
        