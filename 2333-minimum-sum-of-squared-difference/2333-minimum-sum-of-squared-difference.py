import heapq
class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k1: int
        :type k2: int
        :rtype: int
        """

        """diff = []
        k = k1 + k2

        for i in range(len(nums1)):
            d = abs(nums1[i] - nums2[i])
            diff.append(d)

        if sum(diff) <= k:
            return 0

        max_heap = []

        for i in range(len(diff)):
            heapq.heappush(max_heap, -diff[i])

        for i in range(k):
            num = -heapq.heappop(max_heap)
            num -= 1
            heapq.heappush(max_heap, -num)

        ans = 0

        while max_heap:
            num = -heapq.heappop(max_heap)
            ans += num * num

        return ans"""


        diff = []
        k = k1 + k2

        for i in range(len(nums1)):
            d = abs(nums1[i] - nums2[i])
            diff.append(d)

        if sum(diff) <= k:
            return 0

        left = 0
        right = max(diff)

        while left < right:
            mid = (left + right) // 2
            need = 0

            for d in diff:
                if d > mid:
                    need += d - mid

            if need <= k:
                right = mid
            else:
                left = mid + 1

        remaining = k

        for i in range(len(diff)):
            if diff[i] > left:
                remaining -= diff[i] - left
                diff[i] = left

        for i in range(len(diff)):
            if remaining > 0 and diff[i] == left:
                diff[i] -= 1
                remaining -= 1

        ans = 0

        for d in diff:
            ans += d * d

        return ans
