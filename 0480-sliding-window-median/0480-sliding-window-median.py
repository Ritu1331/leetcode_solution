import heapq

class Solution(object):

    def medianSlidingWindow(self, nums, k):

        small = []          # max heap
        large = []          # min heap
        deleted = {}
        ans = []

        size = [0, 0]       # size[0] = small, size[1] = large

        def cleanSmall():
            while small and -small[0] in deleted:
                x = -heapq.heappop(small)
                deleted[x] -= 1

                if deleted[x] == 0:
                    del deleted[x]

        def cleanLarge():
            while large and large[0] in deleted:
                x = heapq.heappop(large)
                deleted[x] -= 1

                if deleted[x] == 0:
                    del deleted[x]

        def balance():

            if size[0] > size[1] + 1:
                x = -heapq.heappop(small)
                heapq.heappush(large, x)

                size[0] -= 1
                size[1] += 1

            elif size[1] > size[0]:
                x = heapq.heappop(large)
                heapq.heappush(small, -x)

                size[1] -= 1
                size[0] += 1

        # First window
        for i in range(k):

            x = nums[i]

            if not small or x <= -small[0]:
                heapq.heappush(small, -x)
                size[0] += 1
            else:
                heapq.heappush(large, x)
                size[1] += 1

            balance()

        # Sliding window
        for i in range(k, len(nums) + 1):

            cleanSmall()
            cleanLarge()

            # Find median
            if k % 2 == 1:
                ans.append(float(-small[0]))
            else:
                ans.append((-small[0] + large[0]) / 2.0)

            if i == len(nums):
                break

            # Remove old number
            old = nums[i - k]

            deleted[old] = deleted.get(old, 0) + 1

            if old <= -small[0]:
                size[0] -= 1
            else:
                size[1] -= 1

            # Add new number
            new = nums[i]

            if new <= -small[0]:
                heapq.heappush(small, -new)
                size[0] += 1
            else:
                heapq.heappush(large, new)
                size[1] += 1

            cleanSmall()
            cleanLarge()

            balance()

        return ans