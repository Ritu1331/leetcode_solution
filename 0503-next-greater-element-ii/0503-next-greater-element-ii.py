class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)

        stack = []
        ans = [0] * n

        # Pre-fill stack for circular traversal
        for i in range(n - 2, -1, -1):
            stack.append(nums[i])

        # Normal Next Greater from right to left
        for i in range(n - 1, -1, -1):

            while stack and stack[-1] <= nums[i]:
                stack.pop()

            if not stack:
                ans[i] = -1
            else:
                ans[i] = stack[-1]

            stack.append(nums[i])

        return ans