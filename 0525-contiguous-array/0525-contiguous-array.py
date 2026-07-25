class Solution(object):
    def findMaxLength(self, nums):
        n = len(nums)
        res = 0
        zero = 0 
        one = 0
        f = {0: -1}   # important initialization

        for i in range(n):
            if nums[i] == 0:
                zero += 1
            else:
                one += 1

            diff = zero - one
 
            if diff in f:
                index = f[diff]
                length = i - index
                res = max(length, res)
            else:
                f[diff] = i   # store first occurrence index

        return res
