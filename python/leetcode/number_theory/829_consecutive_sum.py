"""
829. Consecutive Numbers Sum (Hard)

Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

Example 1:

Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3
Example 2:

Input: 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
Example 3:

Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
Note: 1 <= N <= 10 ^ 9.
"""


class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        i = 1
        result = 0
        while i * i <= N:
            # tackle i
            # case 1: N % i == 0
            if N % i == 0:
                mid = N // i
                if i % 2 == 1 and mid - i // 2 > 0:
                    print(i, mid)
                    result += 1
            else:
                i += 1
                continue
            # case 2: 2i
            j = 2 * i
            if N % j != 0:
                if N // j - (j // 2 - 1) > 0:
                    print(j, N / j)
                    result += 1

            # tackle j = N/i numbers
            j = N // i
            if j <= i:
                i += 1
                continue
            # j numbers
            mid = N // j
            if j % 2 == 1 and mid - j // 2 > 0:
                print(j, mid)
                result += 1
            # 2j numbers
            j = j * 2
            if N % j != 0:
                if N // j - (j // 2 - 1) > 0:
                    print(j, N / j)
                    result += 1
            i += 1
        return result

    def solve2(self, N):
        count = 1
        k = 2
        while k * k < 2 * N:
            if (N - (k * (k - 1) // 2)) % k == 0:
                count += 1
            k += 1
        return count


if __name__ == "__main__":
    a = Solution()
    print(a.consecutiveNumbersSum(15))
