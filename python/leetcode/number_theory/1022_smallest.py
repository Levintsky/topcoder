"""
1022. Smallest Integer Divisible by K (Medium)

Given a positive integer K, you need find the smallest positive integer N such that N is divisible by K, and N only contains the digit 1.

Return the length of N.  If there is no such N, return -1.

Example 1:

Input: 1
Output: 1
Explanation: The smallest answer is N = 1, which has length 1.
Example 2:

Input: 2
Output: -1
Explanation: There is no such positive integer N divisible by 2.
Example 3:

Input: 3
Output: 3
Explanation: The smallest answer is N = 111, which has length 3.
 

Note:
1 <= K <= 10^5
"""

"""
For a given K, we evaluate 1 % K, 11 % K, 111 % K, ..., 11...1 (K '1's) % K.

If any remainder is 0, then the current number is the smallest integer divisible by K.
If none of the remainders is 0, then at some point, there must be some duplicate remainders (due to Pigeonhole principle), as the K remainders can only take at most K-1 different values excluding 0. In this case, no number with the pattern 1...1 is divisible by K. This is because once a remainder has a duplicate, the next remainder will be in a loop, as the previous remainder determines the next_mod, i.e., next_mod = (10 * prev_mod + 1) % K. Therefore, we will never see remainder==0.
A simple example is when K is 6. Once we see 1111 % 6 = 1, we immediately know 11111 % 6 will be 5, since 1 % 6 = 1 and 11 % 6 = 5. Therefore, there will be no such number that is divisible by 6.

1 % 6 = 1
11 % 6 = 5
111 % 6 = 3
1111 % 6 = 1
11111 % 6 = 5
111111 % 6 = 3
"""


import math


class Solution(object):
    def smallestRepunitDivByK(self, K):
        if K == 1:
            return 1
        if K % 2 == 0:
            return -1
        if K % 5 == 0:
            return -1

        # factor of k
        def help(k):
            # return a decomposition of K
            result = []
            begin, end = 3, k + 1
            for j in range(begin, end):
                if k % j == 0:
                    curr = [j, 0]
                    while k % j == 0:
                        curr[-1] += 1
                        k = k // j
                    result.append(curr[0] ** curr[1])
            # print(result)
            if len(result) == 0:
                result = [k]
            return result

        def help2(k):
            # for each item, return length dividable
            i = 1
            while i % k != 0:
                i = i * 10 + 1
            return len(str(i))

        def cdg(m, n):
            m, n = max(m, n), min(m, n)
            if m % n == 0:
                return n
            else:
                return cdg(n, m % n)

        # step 1: factorization:
        result_fact = help(K)
        # step 2: len_ of each item
        result_len = []
        for item in result_fact:
            len_ = help2(item)
            result_len.append(len_)
        # step 3: common diviser of all len_
        final = 1
        for item in result_len:
            cdg_ = cdg(final, item)
            final = final * item // cdg_
        return final


if __name__ == "__main__":
    a = Solution()
    # print(help(189))
    # print(help2(37))
    # print(cdg(12, 30))
    print(a.smallestRepunitDivByK(21))
