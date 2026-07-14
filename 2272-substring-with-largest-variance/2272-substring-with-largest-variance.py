class Solution(object):
    def largestVariance(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0

        chars = set(s)

        # Try every pair of characters
        for major in chars:

            for minor in chars:

                if major == minor:
                    continue

                major_count = 0
                minor_count = 0

                # How many minor characters are still left
                remaining_minor = s.count(minor)

                for ch in s:

                    # Ignore other characters
                    if ch != major and ch != minor:
                        continue

                    if ch == major:

                        major_count += 1

                    else:

                        minor_count += 1
                        remaining_minor -= 1

                    # Update answer only if both chars exist
                    if minor_count > 0:

                        ans = max(
                            ans,
                            major_count - minor_count
                        )

                    # Kadane reset condition
                    if (major_count < minor_count
                            and remaining_minor > 0):

                        major_count = 0
                        minor_count = 0

        return ans