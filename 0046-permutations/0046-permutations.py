class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        ans = []
        def backtrack():

            if len(ans) == len(nums):
                res.append(ans[:])
                return
            
            for i in range(len(nums)):
                if nums[i] in ans:
                    continue

                ans.append(nums[i])

                backtrack()

                ans.pop()

        backtrack()
        return res
        