class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(len(nums)):
            ans = ans ^ nums[i]
        
        return ans 

        