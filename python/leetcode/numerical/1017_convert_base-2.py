"""
1017. Convert to Base -2 (Medium)

Given a number N, return a string consisting of "0"s and "1"s that represents its value in base -2 (negative two).

The returned string must have no leading zeroes, unless the string is "0".

Example 1:

Input: 2
Output: "110"
Explantion: (-2) ^ 2 + (-2) ^ 1 = 2

Example 2:

Input: 3
Output: "111"
Explantion: (-2) ^ 2 + (-2) ^ 1 + (-2) ^ 0 = 3

Example 3:

Input: 4
Output: "100"
Explantion: (-2) ^ 2 = 4
"""


def fastcheck(n_list):
    curr = 0
    base = 1
    for item in n_list:
        curr += item * base
        base *= -2
    return curr


class Solution:
    def baseNeg2(self, N: int) -> str:
        # change to base 2
        if N == 0:
            return "0"
        result = []
        while N > 0:
            result.append(N % 2)
            N //= 2

        # step 2: one time convert to base -2
        n = len(result)
        for i in range(1, n, 2):
            if result[i] == 1:
                if i + 1 < n:
                    result[i + 1] += 1
                else:
                    result.append(1)

        flag = False
        while not flag:  # 1 on (2*i+1)-th digit
            # check no 2 in data
            flag = True
            for idx, item in enumerate(result):
                if item >= 2:
                    result[idx] -= 2
                    if idx + 1 < len(result) and result[idx + 1] > 0:
                        result[idx + 1] -= 1
                    else:
                        # append 2 1s
                        if idx == len(result) - 1:
                            result.append(0)
                        if idx + 1 == len(result) - 1:
                            result.append(0)
                        result[idx + 1] += 1
                        result[idx + 2] += 1
                    flag = False
        print(fastcheck(result))
        result = [str(item) for item in result]
        result = "".join(result)
        result = result[::-1]

        return result


if __name__ == "__main__":
    a = Solution()
    # a.baseNeg2(14)
    for i in range(1, 100):
        print(i, a.baseNeg2(i))
