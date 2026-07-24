class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom = {}
        mag = {}

        for ch in ransomNote:
            ransom[ch] = ransom.get(ch, 0) + 1

        for ch in magazine:
            mag[ch] = mag.get(ch, 0) + 1

        for ch in ransom:

            if mag.get(ch, 0) < ransom[ch]:
                return False

        return True


        '''freq = {}

        # Count letters in magazine
        for ch in magazine:
            freq[ch] = freq.get(ch, 0) + 1

        # Check if ransomNote can be formed
        for ch in ransomNote:

            if freq.get(ch, 0) == 0:
                return False

            freq[ch] -= 1

        return True'''