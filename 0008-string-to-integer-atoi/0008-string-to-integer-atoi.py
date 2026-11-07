class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        sign = 1
        num = 0
        n = len(s)
        i = 0

        # Step 1: Skip leading spaces
        while i < n and s[i] == " ":
            i += 1

        # Step 2: Check sign
        if i < n and s[i] == "-":
            sign = -1
            i += 1
        elif i < n and s[i] == "+":
            i += 1

        # Step 3: Read digits
        while i < n and s[i].isdigit():
            digit = int(s[i])
            num = num * 10 + digit
            i += 1

        # Step 4: Apply sign
        num = num * sign

        # Step 5: Handle overflow
        num = max(-2**31, min(num, 2**31 - 1))

        return num