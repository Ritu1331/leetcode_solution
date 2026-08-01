class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        # Always binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        size1 = len(nums1)
        size2 = len(nums2)

        low = 0
        high = size1

        while low <= high:

            # Partition in first array
            partition1 = (low + high) // 2

            # Partition in second array
            partition2 = (size1 + size2 + 1) // 2 - partition1

            # Left value of first array
            if partition1 == 0:
                leftArray1 = float("-inf")
            else:
                leftArray1 = nums1[partition1 - 1]

            # Right value of first array
            if partition1 == size1:
                rightArray1 = float("inf")
            else:
                rightArray1 = nums1[partition1]

            # Left value of second array
            if partition2 == 0:
                leftArray2 = float("-inf")
            else:
                leftArray2 = nums2[partition2 - 1]

            # Right value of second array
            if partition2 == size2:
                rightArray2 = float("inf")
            else:
                rightArray2 = nums2[partition2]

            # Correct partition found
            if leftArray1 <= rightArray2 and leftArray2 <= rightArray1:

                # Odd number of elements
                if (size1 + size2) % 2 == 1:
                    return max(leftArray1, leftArray2)

                # Even number of elements
                return (max(leftArray1, leftArray2) + min(rightArray1, rightArray2)) / 2.0

            # Too many elements taken from nums1
            elif leftArray1 > rightArray2:
                high = partition1 - 1

            # Too few elements taken from nums1
            else:
                low = partition1 + 1