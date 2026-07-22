class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """

        stack = []

        for num in asteroids:

            # Collision occurs only when:
            # stack top is moving right and current asteroid moves left

            while stack and stack[-1] > 0 and num < 0:

                # Current asteroid is bigger
                if stack[-1] < abs(num):
                    stack.pop()

                # Both have the same size
                elif stack[-1] == abs(num):
                    stack.pop()
                    break

                # Stack top is bigger
                else:
                    break

            else:
                stack.append(num)

        return stack