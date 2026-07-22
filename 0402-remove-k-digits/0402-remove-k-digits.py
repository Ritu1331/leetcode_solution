class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []

        for digit in num:

            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1

            stack.append(digit)

        # If some removals are still left
        while k > 0:
            stack.pop()
            k -= 1

        ans = ""

        for digit in stack:
            ans += digit

        # Remove leading zeros
        ans = ans.lstrip("0")

        if ans == "":
            return "0"

        return ans


        ans = "000123"

"""without builtin function    
i = 0

while i < len(ans) and ans[i] == "0":
    i += 1

ans = ans[i:]

print(ans)"""