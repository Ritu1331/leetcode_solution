class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        low = 1
        high = m * n

        while low < high:

            mid = (low + high) // 2

            count = 0

            for i in range(1, m + 1):
                count += min(mid // i, n)

            if count < k:
                low = mid + 1
            else:
                high = mid

        return low
        