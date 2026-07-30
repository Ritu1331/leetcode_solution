class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix) - 1
        col = 0

        while row >= 0 and col < len(matrix[0]):

            if matrix[row][col] == target:
                return True

            elif target < matrix[row][col]:
                row -= 1      # move up

            else:
                col += 1      # move right

        return False
        
        