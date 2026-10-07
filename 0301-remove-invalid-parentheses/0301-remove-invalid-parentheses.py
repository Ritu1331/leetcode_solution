from collections import deque

class Solution(object):
    def removeInvalidParentheses(self, s):

        def isValid(s):
            balance = 0

            for ch in s:
                if ch == "(":
                    balance += 1

                elif ch == ")":
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        queue = deque([s])
        visited = {s}
        ans = []

        while queue:
            size = len(queue)

            for _ in range(size):
                current = queue.popleft()

                if isValid(current):
                    ans.append(current)

                if ans:
                    continue

                for i in range(len(current)):

                    if current[i] not in "()":
                        continue

                    new_string = current[:i] + current[i + 1:]

                    if new_string not in visited:
                        visited.add(new_string)
                        queue.append(new_string)

            if ans:
                return ans

        return ans