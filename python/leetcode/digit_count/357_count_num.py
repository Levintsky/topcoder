'''
357. Count Numbers with Unique Digits (Medium)

Given a non-negative integer n, count all numbers with unique digits, x, where 0 <= x < 10^n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 <= x < 100, excluding [11,22,33,44,55,66,77,88,99])
'''

class Solution(object):
  def countNum(self, n):
    if n == 0: return 0

    cnt_w = [0, 10, 81] # x: with unique
    cnt_wo = [0, 0, 9] # y: without unique
    cnt_w0 = [0, 1, 9] # z: unique with 0
    # n-digit:
    # x[n] = 9*9*8*...
    x = [0, 10]
    for i in range(2, n+1):
      tmp = 9
      for j in range(i-1):
        tmp *= (9-j)
      x.append(tmp)
    return sum(x)


if __name__ == '__main__':
  a = Solution()
  print a.countNum(3)
