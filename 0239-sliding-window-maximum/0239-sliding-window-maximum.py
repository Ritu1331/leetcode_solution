from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):

        dq = deque()
        res = []

        for i in range(len(nums)):

            # Step 1
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Step 2
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # Step 3
            dq.append(i)

            # Step 4
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res