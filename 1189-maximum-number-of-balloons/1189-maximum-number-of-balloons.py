class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        freq = {}

        for ch in text:
            freq[ch] = freq.get(ch, 0) + 1

        need = {
        'b': 1,
        'a': 1,
        'l': 2,
        'o': 2,
        'n': 1
        }

        res = float('inf')

        for ch, fneed in need.items():
            fhave = freq.get(ch, 0)
            times = fhave // fneed
            res = min(res, times)

        return res
        