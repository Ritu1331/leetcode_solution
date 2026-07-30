class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        low = 1
        high = max(candies)
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            children = 0
            for piles in candies:
                children += piles // mid

            if children >= k:
                ans = mid
                low = mid + 1
                
            else:
                high = mid - 1
                
        return ans

        