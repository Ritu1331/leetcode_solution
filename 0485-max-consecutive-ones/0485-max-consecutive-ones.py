class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low =0
        n = len(nums)
        
        max_count = 0
        for high in range(n):
            if nums[high] == 1:
                length = high - low + 1
                max_count = max(max_count , length) 
                
            
            else:
                low = high + 1
              
        
        return max_count

        