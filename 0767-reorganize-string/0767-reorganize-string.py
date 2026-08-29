import heapq

class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        heap = []

        for ch, count in freq.items():
            heapq.heappush(heap, (-count, ch))

        res = ""

        prev_count = 0
        prev_char = ""

        while heap:

            count, ch = heapq.heappop(heap)

            res += ch

            # put previous character back into heap
            if prev_count < 0:
                heapq.heappush(heap, (prev_count, prev_char))

            # one occurrence of current character used
            count += 1

            prev_count = count
            prev_char = ch

        if len(res) != len(s):
            return ""

        return res