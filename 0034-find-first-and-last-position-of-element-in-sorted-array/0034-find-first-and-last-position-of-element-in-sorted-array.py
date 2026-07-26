class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low = 0
        high = len(nums)-1
        first = -1
        last = -1

        while low<=high:
            mid = (low + high ) // 2
            if target == nums[mid]:
                first = mid
                high = mid - 1
            
            elif target < nums[mid]:
                high = mid -1
            
            else:
                low = mid + 1
        
        low = 0
        high = len(nums) -1

        while low<=high:
            mid = (low + high ) // 2
            if target == nums[mid]:
                last = mid
                low = mid +1
            
            elif target < nums[mid]:
                high = mid -1
            
            else:
                low = mid + 1
        return [first , last]

                

        