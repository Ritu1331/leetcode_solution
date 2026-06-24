class Solution:
    def generateParenthesis(self, n):

        res = []

        def backtrack(open_count, close_count, temp):

            if open_count == n and close_count == n:
                res.append(temp)
                return

            # Add '('
            if open_count < n:
                backtrack(
                    open_count + 1,
                    close_count,
                    temp + "("
                )

            # Add ')'
            if close_count < open_count:
                backtrack(
                    open_count,
                    close_count + 1,
                    temp + ")"
                )

        backtrack(0, 0, "")
        return res