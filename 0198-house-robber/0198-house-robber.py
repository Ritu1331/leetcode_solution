class Solution(object):

    def __init__(self):
        self.dp = {}

    def rob(self, nums):
        n = len(nums)
        return self.calc(nums, n, 0, 1)

    def calc(self, nums, n, i, free):

        if i == n:
            return 0

        if (i, free) in self.dp:
            return self.dp[(i, free)]

        if free == 0:
            ans = self.calc(nums, n, i + 1, 1)
        else:
            c1 = nums[i] + self.calc(nums, n, i + 1, 0)
            c2 = self.calc(nums, n, i + 1, 1)
            ans = max(c1, c2)

        self.dp[(i, free)] = ans
        return ans