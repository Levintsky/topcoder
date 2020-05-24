"""
902. Numbers At Most N Given Digit Set (Hard)

We have a sorted set of digits D, a non-empty subset of {'1','2','3','4','5','6','7','8','9'}.  (Note that '0' is not included.)

Now, we write numbers using these digits, using each digit as many times as we want.  For example, if D = {'1','3','5'}, we may write numbers such as '13', '551', '1351315'.

Return the number of positive integers that can be written (using the digits of D) that are less than or equal to N.

 

Example 1:

Input: D = ["1","3","5","7"], N = 100
Output: 20
Explanation: 
The 20 numbers that can be written are:
1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
Example 2:

Input: D = ["1","4","9"], N = 1000000000
Output: 29523
Explanation: 
We can write 3 one digit numbers, 9 two digit numbers, 27 three digit numbers,
81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit numbers.
In total, this is 29523 integers that can be written using the digits of D.
 

Note:

D is a subset of digits '1'-'9' in sorted order.
1 <= N <= 10^9
"""

class Solution(object):
    def atMostNGivenDigitSet(self, D, N):
        """
        :type D: List[str]
        :type N: int
        :rtype: int
        """
        # step 1: how many digits (n digits)
        Nlist = []
        while N > 0:
            Nlist.append(N % 10)
            N //= 10
        Nlist = Nlist[::-1]
        n = len(Nlist)
        
        result = sum([len(D) ** i for i in range(1, n)])
        D = [int(item) for item in D]
        for i, item in enumerate(Nlist):
            tmp = len([j for j in D if j < item])
            tmp *= len(D) ** (n-i-1)
            result += tmp
            # special case
            if i == n-1 and item in D:
                result += 1
            if item not in D:
                break
        
        return result


if __name__ == "__main__":
    a = Solution()
    print(a.atMostNGivenDigitSet(["1","3","5","7"], 100))
    print(a.atMostNGivenDigitSet(["1","4", "9"], 1000000000))
    print(a.atMostNGivenDigitSet(["3","4", "8"], 4))
    print(a.atMostNGivenDigitSet(["3","4", "8"], 243646758))
