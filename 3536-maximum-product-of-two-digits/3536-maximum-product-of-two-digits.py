class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''digits = []

        while n > 0:
            digits.append(n % 10)
            n //= 10

        digits.sort()

        return digits[-1] * digits[-2]'''

        largest = -1
        secondLargest = -1

        while n > 0:

            digit = n % 10

            if digit >= largest:
                secondLargest = largest
                largest = digit

            elif digit > secondLargest:
                secondLargest = digit

            n //= 10

        return largest * secondLargest

