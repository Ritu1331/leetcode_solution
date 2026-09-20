class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        digitseen = False
        dotseen = False
        eseen = False

        for i in range(len(s)):
            c = s[i]

            if c.isdigit():
                digitseen = True

            elif c == '.':
                if dotseen or eseen:
                    return False

                dotseen = True

            elif c == 'e' or c == 'E':
                if eseen or not digitseen:
                    return False

                eseen = True
                digitseen = False

            elif c == '+' or c == '-':
                if i != 0 and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False

            else:
                return False

        return digitseen