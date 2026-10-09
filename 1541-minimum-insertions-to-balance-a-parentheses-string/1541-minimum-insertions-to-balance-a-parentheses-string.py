class Solution(object):
    def minInsertions(self, s):
        ans = 0
        need = 0

        for ch in s:
            if ch == "(":
                need += 2

                if need % 2 == 1:
                    ans += 1
                    need -= 1

            else:
                need -= 1

                if need < 0:
                    ans += 1
                    need = 1

        return ans + need