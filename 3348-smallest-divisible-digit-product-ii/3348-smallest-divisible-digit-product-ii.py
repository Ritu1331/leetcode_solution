class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def smallestNumber(self, num, t):
        temp = t

        for i in range(2, 10):
            while temp % i == 0:
                temp //= i

        if temp > 1:
            return "-1"

        n = len(num)
        rem = [0] * (n + 1)
        rem[0] = t

        pos = n - 1
        num_list = list(num)

        for i in range(n):
            if num_list[i] == "0":
                pos = i
                break

            rem[i + 1] = rem[i] // self.gcd(rem[i], int(num_list[i]))

        if rem[n] == 1:
            return num

        for i in range(pos, -1, -1):

            while True:

                num_list[i] = chr(ord(num_list[i]) + 1)

                if num_list[i] > "9":
                    break

                remaining = rem[i] // self.gcd(rem[i], int(num_list[i]))

                k = 9

                for j in range(n - 1, i, -1):

                    while k > 1 and remaining % k != 0:
                        k -= 1

                    if k == 1:
                        num_list[j] = "1"
                    else:
                        remaining //= k
                        num_list[j] = str(k)

                if remaining == 1:
                    return "".join(num_list)

        ans = []
        original = t

        for i in range(9, 1, -1):
            while original % i == 0:
                ans.append(str(i))
                original //= i

        while len(ans) < n + 1:
            ans.append("1")

        ans.reverse()

        return "".join(ans)