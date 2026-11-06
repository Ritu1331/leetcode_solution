class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        count = 0

        for i in range(len(arr1)):

            valid = True

            for j in range(len(arr2)):

                if abs(arr1[i] - arr2[j]) <= d:
                    valid = False
                    break

            if valid:
                count += 1

        return count