class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        k = 1
        for i in range(n):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k+=1
        

        return k


            
        