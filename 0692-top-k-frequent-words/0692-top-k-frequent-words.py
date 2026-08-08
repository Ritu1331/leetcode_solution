import heapq

class Solution(object):
    def topKFrequent(self, words, k):

        freq = {}

        for word in words:
            freq[word] = freq.get(word, 0) + 1

        heap = []

        for word, count in freq.items():
            heapq.heappush(heap, (-count, word))

        ans = []

        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans