class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        f = {0:1}
        res=0
        prefix_sum = 0
        for i in range (n):
            prefix_sum+=nums[i]
            rem = (prefix_sum%k)
            # handle negative case
            if rem < 0:
                rem += k
            if rem in f:
                res+=f[rem]

            f[rem] = f.get(rem,0)+1
        
        return res


        