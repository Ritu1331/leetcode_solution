class Solution(object):

    def kadane(self, gain):

        curr = 0
        best = 0

        for num in gain:

            curr = max(0, curr + num)

            best = max(best, curr)

        return best

    def maximumsSplicedArray(self, nums1, nums2):

        n = len(nums1)

        gain1 = [0] * n

        for i in range(n):

            gain1[i] = nums2[i] - nums1[i]

        gain2 = [0] * n

        for i in range(n):

            gain2[i] = nums1[i] - nums2[i]

        ans = max(

            sum(nums1) + self.kadane(gain1),

            sum(nums2) + self.kadane(gain2)

        )

        return ans