class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Length of string and pattern
        m = len(s)
        n = len(p)

        # Create DP table
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Empty string matches empty pattern
        dp[0][0] = True

        # Handle patterns like a*, a*b*, a*b*c*
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # Check every string character
        for i in range(1, m + 1):

            # Check every pattern character
            for j in range(1, n + 1):

                # Case 1: Same character or dot
                if p[j - 1] == '.' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

                # Case 2: Star
                elif p[j - 1] == '*':
                    
                    # Option 1: Use zero occurrences
                    dp[i][j] = dp[i][j - 2]

                    # Option 2: Use one or more occurrences
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

        # Return final answer
        return dp[m][n]
        