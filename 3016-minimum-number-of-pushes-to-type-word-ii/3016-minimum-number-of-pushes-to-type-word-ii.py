class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        freq = {}

        # Count frequency
        for ch in word:
            freq[ch] = freq.get(ch, 0) + 1

        # Sort frequencies
        frequencies = sorted(freq.values(), reverse=True)

        ans = 0

        for i in range(len(frequencies)):
            pushes = (i // 8) + 1
            ans += frequencies[i] * pushes

        return ans
        