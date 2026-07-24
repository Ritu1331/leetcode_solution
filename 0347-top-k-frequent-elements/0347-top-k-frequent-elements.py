import heapq

class Solution(object):
    def topKFrequent(self, nums, k):

        '''freq = {}

        # Count frequency
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        heap = []

        # Keep min heap of size k
        for num, count in freq.items():

            heapq.heappush(heap, (count, num))

            if len(heap) > k:
                heapq.heappop(heap)

        ans = []

        while heap:
            ans.append(heapq.heappop(heap)[1])

        return ans'''

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            bucket[count].append(num)

        ans = []

        for i in range(len(bucket) - 1, 0, -1):

            for num in bucket[i]:
                ans.append(num)

                if len(ans) == k:
                    return ans