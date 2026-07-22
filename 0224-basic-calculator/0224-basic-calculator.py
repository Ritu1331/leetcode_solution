class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        stack = []
        result = 0
        number = 0
        sign = 1

        for ch in s:
            if ch.isdigit():
                number = number * 10 + int(ch)
            
            elif ch == "+":
                result = result + sign * number

                number = 0
                sign = 1
            
            elif ch == "-":
                result = result + sign * number

                number = 0
                sign = -1
            
            elif ch == "(":
                stack.append(result)
                stack.append(sign)

                result = 0
                sign = 1
            
            elif ch == ")":
                result = result + sign * number

                number = 0

                prev_sign = stack.pop()
                
                prev_result = stack.pop()

                result = prev_result + prev_sign * result

        result += sign * number

        return result

            
