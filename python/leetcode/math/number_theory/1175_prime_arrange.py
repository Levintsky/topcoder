"""
1175. Prime Arrangements (Easy)

Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)

(Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers both smaller than it.)

Since the answer may be large, return the answer modulo 10^9 + 7.

Example 1:

Input: n = 5
Output: 12
Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.
Example 2:

Input: n = 100
Output: 682289015
 

Constraints:

1 <= n <= 100
"""

class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        memo = [True] * (n+1) # 1-indexed
        memo[1] = False
        for i in range(2, n):
            for j in range(2, n//i+1):
                memo[i*j] = False
        memo = memo[1:]
        n_prime, n_non = 0, 0
        for item in memo:
            if item:
                n_prime += 1
            else:
                n_non += 1
        MOD = 10 ** 9 + 7
        # n_prime
        print(n_prime, n_non)
        def factor(i):
            if i in [0, 1]:
                return 1
            res = 1
            for j in range(2, i+1):
                res = (res * j) % MOD
            return res
        result = (factor(n_prime) * factor(n_non)) % MOD
        return result


if __name__ == "__main__":
    a = Solution()
    print(a.numPrimeArrangements(100))