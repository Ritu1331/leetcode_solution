class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new = []
        seen = set(nums)
        
        for num in nums:
            if nums - 1 in seen:
                curr = nums
            while nums:
                new.append(nums + 1)
        
        return new