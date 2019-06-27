"""
600. Non-negative Integers without Consecutive Ones (Hard)

Given a positive integer n, find the number of non-negative integers less than or equal to n, whose binary representations do NOT contain consecutive ones.

Example 1:
Input: 5
Output: 5
Explanation: 
Here are the non-negative integers <= 5 with their corresponding binary representations:
0 : 0
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule. 
Note: 1 <= n <= 10**9
"""

"""
no consecutive 1s starting with 0 and 1 as a[i], b[i]
a[i] = a[i-1] + b[i-1]
b[i] = a[i-1]

then minus all results with nth digit but larger than num
"""


class Solution(object):
    def solution2(self, num):
        sb = self.binarize(num)
        sb = sb[::-1]
        n = len(sb)

        a, b = [0] * n, [0] * n
        a[0], b[0] = 1, 1
        for i in range(1, n):
            a[i] = a[i - 1] + b[i - 1]
            b[i] = a[i - 1]

        result = a[-1] + b[-1]
        i = n - 2
        while i >= 0:
            if sb[i] == 1 and sb[i + 1] == 1:
                break
            if sb[i] == 0 and sb[i + 1] == 0:
                result -= b[i]
            i -= 1
        return result

    def findIntegers(self, num):
        """
    :type num: int
    :rtype: int
    """
        if num == 0:
            return 1
        if num == 1:
            return 2
        if num == 2:
            return 3
        cnt = self.helper(num)  # how many digit
        # rec[i]: how many number with <= i-digits satisfy no consecutive 1
        rec = [2, 1]

        for i in range(3, cnt + 1):
            tmp = sum(rec[:-1])
            rec.append(tmp)
        result = sum(rec)

        print(rec)
        # binary represent of current n
        n_bin = self.binarize(num)
        n = len(n_bin)
        print(n_bin)
        i = 1
        while i < n:
            # 2 consecutive ones: break
            if n_bin[i] == 1 and n_bin[i - 1] == 1:
                break
            elif n_bin[i] == 0 and n_bin[i - 1] == 0:
                print(rec[n - i - 1])
                result -= rec[n - i - 1]
            i += 1
        # finally, if it ends with 00, plus one
        if i == n and n_bin[-1] == 0 and n_bin[-2] == 0:
            result += 1
        return result

    def binarize(self, num):
        result = []
        while num != 0:
            result.append(num % 2)
            num //= 2
        result = result[::-1]
        return result

    def helper(self, num):
        # decide how many digits
        if num == 0:
            return 1
        cnt = 0
        while num > 0:
            num /= 2
            cnt += 1
        return cnt


if __name__ == "__main__":
    a = Solution()
    # print a.findIntegers(64)
    print(a.solution2(2))
