class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        memo = {}

        def solve(left, right):

            # Only one number left
            if left == right:
                return nums[left]

            if (left, right) in memo:
                return memo[(left, right)]

            # Pick left number
            takeLeft = nums[left] - solve(left + 1, right)

            # Pick right number
            takeRight = nums[right] - solve(left, right - 1)

            memo[(left, right)] = max(takeLeft, takeRight)

            return memo[(left, right)]

        return solve(0, len(nums) - 1) >= 0
        