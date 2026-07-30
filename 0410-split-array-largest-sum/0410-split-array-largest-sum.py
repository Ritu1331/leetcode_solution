class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        low = max(nums)
        high = sum(nums)
        ans = high

        while low <= high :
            mid = (low + high ) // 2

            curr_sum = 0
            group =  1

            for num in nums:
                curr_sum += num

                if curr_sum > mid:
                    group += 1
                    curr_sum = num
                
            if group > k:
                low = mid + 1
                
            else:
                ans = mid
                high = mid - 1
                
        return ans 
        