class Solution:

    # Calculate nCr (Combination)
    # Stop early if answer becomes greater than limit
    def combination(self, n, r, limit):

        r = min(r, n - r)
        answer = 1

        for i in range(1, r + 1):
            answer = answer * (n - r + i) // i

            if answer > limit:
                return limit + 1

        return answer


    # Count how many different left halves can be formed
    def countWays(self, freq, remaining, limit):

        ways = 1

        for count in freq:

            if count == 0:
                continue

            ways *= self.combination(remaining, count, limit)

            if ways > limit:
                return limit + 1

            remaining -= count

        return ways


    def smallestPalindrome(self, s, k):

        # Frequency of every character
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        n = len(s)
        halfLength = n // 2

        answer = [""] * n

        # Find middle character and keep only half frequencies
        for i in range(26):

            if freq[i] % 2 == 1:
                answer[halfLength] = chr(i + ord('a'))

            freq[i] //= 2

        # Total possible palindromes
        if self.countWays(freq, halfLength, k) < k:
            return ""

        # Build left half greedily
        for pos in range(halfLength):

            for ch in range(26):

                if freq[ch] == 0:
                    continue

                # Try placing this character
                freq[ch] -= 1

                possible = self.countWays(
                    freq,
                    halfLength - pos - 1,
                    k
                )

                if possible >= k:

                    answer[pos] = chr(ch + ord('a'))
                    break

                k -= possible
                freq[ch] += 1

        # Copy left half to right half
        for i in range(halfLength):
            answer[n - 1 - i] = answer[i]

        return "".join(answer)