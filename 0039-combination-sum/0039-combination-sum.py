class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def backtrack(idx, path, total):

            # Base Case
            if idx == len(candidates):
                if total == target:
                    res.append(path[:])
                return

            # Choice 1 : Skip current number
            backtrack(idx + 1, path, total)

            # Choice 2 : Take current number
            if total + candidates[idx] <= target:

                path.append(candidates[idx])

                backtrack(idx, path, total + candidates[idx])

                path.pop()

        backtrack(0, [], 0)

        return res
        