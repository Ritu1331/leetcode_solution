class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        left = 0
        right = int(c ** 0.5)

        while left <= right :
            total = left ** 2 + right ** 2

            if total == c:
                return True
            
            if total < c:
                left += 1
            else:
                right -= 1
        
        return False

        