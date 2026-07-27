class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """nums.sort()
        num1 = nums[-1]
        nums2 = nums[-2]

        return ((nums[-1]-1) * (nums[-2] - 1))
        """
        max1 = nums[0]
        max2 = 0

        n = len(nums)
        for i in range(1 , n):
            if nums[i] > max1:
                max2 = max1
                max1 = nums[i]
                
            elif nums[i] > max2:
                max2 = nums[i]
            
        max_value = ((max1 - 1) * (max2 - 1))
        
        return max_value

