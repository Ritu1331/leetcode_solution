class Solution(object):
    def validSequence(self, word1, word2):
        n = len(word1)
        m = len(word2)

        # suf[i] = position where word2[i] can be matched
        # from the right side
        suf = [-1] * m

        j = m - 1

        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                suf[j] = i
                j -= 1

        ans = []
        j = 0
        changed = False

        for i in range(n):

            if j == m:
                break

            # Normal matching character
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            # Use our one allowed mismatch
            elif word1[i] != word2[j] and changed == False:
                
                # If this is the last character,
                # no suffix needs to be matched.
                if j == m - 1:
                    ans.append(i)
                    j += 1
                    changed = True

                # Otherwise, make sure remaining word2
                # can be matched after i
                elif suf[j + 1] != -1 and i < suf[j + 1]:
                    ans.append(i)
                    j += 1
                    changed = True

        if j == m:
            return ans

        return []