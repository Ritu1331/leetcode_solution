class Solution(object):
    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)
        memo = {}

        def dfs(i):
            if i == n:
                return 0

            if i in memo:
                return memo[i]

            best = float("-inf")
            curr = 0

            for k in range(3):
                if i + k < n:
                    curr += stoneValue[i + k]
                    best = max(best, curr - dfs(i + k + 1))

            memo[i] = best
            return best

        diff = dfs(0)

        if diff > 0:
            return "Alice"
        elif diff < 0:
            return "Bob"
        else:
            return "Tie"