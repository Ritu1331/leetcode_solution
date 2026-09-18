class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        from collections import deque
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        q = deque()
        q.append((beginWord, 1))

        while q:

            word, steps = q.popleft()

            if word == endWord:
                return steps

            for i in range(len(word)):

                for ch in "abcdefghijklmnopqrstuvwxyz":

                    newWord = word[:i] + ch + word[i+1:]

                    if newWord in wordSet:

                        q.append((newWord, steps + 1))

                        wordSet.remove(newWord)

        return 0
        