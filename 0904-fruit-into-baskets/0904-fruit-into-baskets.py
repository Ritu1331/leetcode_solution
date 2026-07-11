class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """

        n = len(fruits)
        k = 2
        low = 0
        high = 0
        res = -1
        f = {}   # frequency dictionary

        for high in range(0, n):
            # add character to map
            f[fruits[high]] = f.get(fruits[high], 0) + 1

            # shrink window if more than k distinct
            while len(f) > k:
                f[fruits[low]] -= 1
                if f[fruits[low]] == 0:
                    del f[fruits[low]]
                low += 1

            # update result when exactly k distinct
            if len(f) == k or len(f)<k :
                res = max(res, high - low + 1)

        return res

        