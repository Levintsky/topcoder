"""
866. Prime Palindrome (Medium)

Find the smallest prime palindrome greater than or equal to N.

Recall that a number is prime if it's only divisors are 1 and itself, and it is greater than 1. 

For example, 2,3,5,7,11 and 13 are primes.

Recall that a number is a palindrome if it reads the same from left to right as it does from right to left. 

For example, 12321 is a palindrome.

Example 1:

Input: 6
Output: 7
Example 2:

Input: 8
Output: 11
Example 3:

Input: 13
Output: 101
 
Note:

1 <= N <= 10^8
The answer is guaranteed to exist and be less than 2 * 10^8.
"""

class Solution(object):
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        tmp = [2, 3, 5, 7, 11]
        for item in tmp:
            if N <= item:
                return item
        sN = str(N)
        n = len(sN) // 2
        
        # find the number
        start = 10 ** (n-1)
        for left in range(start, 9999):
            for mid in range(0, 10):
                sl = str(left)
                num = int(sl + str(mid) + sl[::-1])
                if num < N:
                    continue
                if self.check_prime(num):
                    return num
        return -1
                
    def check_prime(self, num):
        i = 2
        while i * i <= num:
            if num % i == 0:
                return False
            i += 1
        return True
