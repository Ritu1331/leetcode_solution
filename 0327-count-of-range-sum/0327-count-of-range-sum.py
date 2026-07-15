class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """

        """prefix sum + merge sort"""
        prefix = [0]

        for num in nums:
            prefix.append(prefix[-1] + num)

        def merge_sort(left, right):

            if left >= right:
                return 0

            mid = (left + right) // 2

            count = merge_sort(left, mid)
            count += merge_sort(mid + 1, right)

            start = mid + 1
            end = mid + 1

            # Count valid pairs
            for i in range(left, mid + 1):

                while start <= right and prefix[start] - prefix[i] < lower:
                    start += 1

                while end <= right and prefix[end] - prefix[i] <= upper:
                    end += 1

                count += end - start

            # Merge step
            temp = []

            p1 = left
            p2 = mid + 1

            while p1 <= mid and p2 <= right:

                if prefix[p1] <= prefix[p2]:
                    temp.append(prefix[p1])
                    p1 += 1
                else:
                    temp.append(prefix[p2])
                    p2 += 1

            while p1 <= mid:
                temp.append(prefix[p1])
                p1 += 1

            while p2 <= right:
                temp.append(prefix[p2])
                p2 += 1

            prefix[left:right + 1] = temp

            return count

        return merge_sort(0, len(prefix) - 1)