'''
400. Nth Digit (Easy)

Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
'''

import math


class Solution(object):
    def findNthDigit(self, n):
      # 1-9: 1-9; cumul (9)
      # 10-99: cumul + 90 x 2; cumul 189
      # 100-999: cumul + 900 x 3; cumul
      i = 1
      cumul = 0

      while(i<11): # i-digit case
        cumul_after = cumul + i*9*(10**(i-1))
        if n>=cumul and n<=cumul_after:
          # figure out which number
          start = 10**(i-1)
          num = start + (n-cumul+i-1) // i - 1
          print(start, num)
          # figure out which digit
          k = (n-cumul-1) % i
          return int(str(num)[k])
        else:
          cumul = cumul_after
          i += 1
      return result

    def solve2(self, n):
        len_ = 1
        count = 9
        start = 1

        while n > len_ * count:
            n -= len_ * count
            len_ += 1
            count *= 10
            start *= 10

        start += (n - 1) // len_
        s = str(start)
        idx = (n - 1) % len_
        return int(s[idx])


if __name__ == '__main__':
  a = Solution()
  # print(a.findNthDigit(5))
  # print(a.findNthDigit(11))
  print(a.solve2(1234))