class Solution(object):
    def findMaxAverage(self, nums, k):
        n = len(nums)
        low = 0
        high = k-1
        avg = 0
       

        for i in range(0, k):
            avg += nums[i]

        res = avg  # only after full window

        while(high < n):
            low += 1
            high += 1
            if(high==n):
                break

            avg = avg - nums[low-1]
            avg += nums[high]
            res = max(res, avg)

        return float(res) / float(k)
