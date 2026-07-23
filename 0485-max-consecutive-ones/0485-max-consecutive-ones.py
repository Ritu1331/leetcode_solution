class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low =0
        n = len(nums)
        count = 0
        max_count = 0
        for high in range(n):
            if nums[high] == 1:
                count += 1
                length = high - low + 1
                max_count = max(max_count , count) 
                
            
            else:
                low = high + 1
                count = 0

         

        
        return max_count

        