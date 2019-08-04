'''
231 Power of Two (Easy)

Given an integer, write a function to determine if it is a power of two.
'''

class Solution(object):
  def isPowerOfTwo(self, n):
    if n<=0:
      return False
    if n & (n-1) == 0:
      return True
    else:
      return False


if __name__ == '__main__':
  a = Solution()
  print a.isPowerOfTwo(0)
  print a.isPowerOfTwo(-1)
  print a.isPowerOfTwo(1)
  print a.isPowerOfTwo(32)
  print a.isPowerOfTwo(65)
