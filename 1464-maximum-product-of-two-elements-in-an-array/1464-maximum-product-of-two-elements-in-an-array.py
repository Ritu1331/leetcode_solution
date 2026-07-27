class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        num1 = nums[-1]
        nums2 = nums[-2]

        return ((nums[-1]-1) * (nums[-2] - 1))
        