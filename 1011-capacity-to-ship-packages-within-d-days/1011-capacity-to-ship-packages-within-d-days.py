class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """

        low = max(weights)
        high = sum(weights)
        ans = high

        while low <= high:

            mid = (low + high) // 2

            daysUsed = 1
            current = 0

            for weight in weights:

                current += weight

                if current > mid:
                    daysUsed += 1
                    current = weight

            if daysUsed <= days:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans