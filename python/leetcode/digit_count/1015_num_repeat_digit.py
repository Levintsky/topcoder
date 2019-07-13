"""
1015. Numbers With 1 Repeated Digit (Hard)

Given a positive integer N, return the number of positive integers less than or equal to N that have at least 1 repeated digit. 

Example 1:

Input: 20
Output: 1
Explanation: The only positive number (<= 20) with at least 1 repeated digit is 11.
Example 2:

Input: 100
Output: 10
Explanation: The positive numbers (<= 100) with atleast 1 repeated digit are 11, 22, 33, 44, 55, 66, 77, 88, 99, and 100.
Example 3:

Input: 1000
Output: 262
 

Note:

1 <= N <= 10^9
"""


class Solution(object):
    def numDupDigitsAtMostN(self, N):
        """
        :type N: int
        :rtype: int
        """

        # f[i]: i-digit, how many non-repeating
        stat = [0, 9]
        for i in range(2, 11):
            stat.append(stat[-1] * (11 - i))
        print(stat)

        # step 2: break N into len_N digit
        N_ori = N
        N_digit = []
        while N > 0:
            N_digit.append(N % 10)
            N //= 10
        N_digit = N_digit[::-1]
        len_N = len(N_digit)

        # result record len = len_N
        print(N_digit)
        result = 0
        for i in range(len_N + 1):
            # keep 0..(i-1)-th digit, change i-th digit
            # how many non-repeating
            subset = set(N_digit[:i])
            # valid?
            if i == len_N:  # keep until last digit
                if len(subset) == i:
                    result += 1
            elif len(subset) == i and N_digit[i] > 0:
                if i == 0:
                    valid_set = set([item for item in range(1, N_digit[i])])
                else:
                    valid_set = set([item for item in range(N_digit[i])])
                valid_set = valid_set - subset
                curr = len(valid_set)

                # check i+1 .. len_N-1 -th digit
                j = i + 1
                base = 9 - i  # already selected, so remaining 10-(i+1)
                while j < len(N_digit):
                    curr *= base
                    base -= 1
                    j += 1
                result += curr
                print(i, curr, result)
        result = N_ori - 10 ** (len_N - 1) - result + 1
        print(result)
        print("###")

        # add all len < len_N
        for i in range(2, len_N):
            item = 9 * 10 ** (i - 1) - stat[i]
            result += item
            print(item, result)
        return result


if __name__ == "__main__":
    a = Solution()

    print(a.numDupDigitsAtMostN(3))
