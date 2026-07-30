class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
    
        m = len(matrix)  ##no of row
        n = len(matrix[0])  ##no of column

        left = 0
        right = m * n - 1

        while left <= right:

            mid = (left + right) // 2

            row = mid // n
            col = mid % n

            num = matrix[row][col]

            if num == target:
                return True

            elif num < target:
                left = mid + 1

            else:
                right = mid - 1

        return False
        