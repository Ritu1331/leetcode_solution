class Solution(object):
    def stoneGameII(self, piles):
        n = len(piles)

        # suffix[i] = sum of piles from i to end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        memo = {}

        def dp(i, M):

            # No piles left
            if i >= n:
                return 0

            # Already calculated
            if (i, M) in memo:
                return memo[(i, M)]

            best = 0

            # Current player can take 1 to 2*M piles
            max_take = min(2 * M, n - i)

            for X in range(1, max_take + 1):

                # New M after taking X piles
                newM = max(M, X)

                # Opponent's best score
                opponent = dp(i + X, newM)

                # Current player's score
                current = suffix[i] - opponent

                # Choose the best option
                best = max(best, current)

            memo[(i, M)] = best

            return best

        return dp(0, 1)