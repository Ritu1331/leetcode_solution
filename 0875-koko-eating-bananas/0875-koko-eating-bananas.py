class Solution(object):
    def minEatingSpeed(self, piles, h):

        low = 1
        high = max(piles)
        ans = high

        while low <= high:

            mid = (low + high) // 2

            hours = 0

            for pile in piles:
                hours += (pile + mid - 1) // mid

            if hours <= h:
                ans = mid          # Store current valid speed
                high = mid - 1     # Try to find a smaller valid speed
            else:
                low = mid + 1      # Need a larger speed

        return ans