class Solution(object):
    def largestVariance(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0

        for a in set(s):
            for b in set(s):

                if a == b:
                    continue

                countA = 0
                countB = 0
                remainB = s.count(b)

                for ch in s:

                    if ch != a and ch != b:
                        continue

                    if ch == a:
                        countA += 1
                    else:
                        countB += 1
                        remainB -= 1

                    if countB > 0:
                        ans = max(ans, countA - countB)

                    if countA < countB and remainB > 0:
                        countA = 0
                        countB = 0

        return ans
        