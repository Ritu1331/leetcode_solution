class Solution(object):

    def __init__(self):
        self.dp = {}

    def dfs(self, i, n):

        # Reached destination
        if i == n:
            return 1

        # Crossed destination
        if i > n:
            return 0

        # Already computed
        if i in self.dp:
            return self.dp[i]

        ans1 = self.dfs(i + 1, n)
        ans2 = self.dfs(i + 2, n)

        self.dp[i] = ans1 + ans2

        return self.dp[i]

    def climbStairs(self, n):
        return self.dfs(0, n)