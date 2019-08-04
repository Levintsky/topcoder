'''
342 Power of Four (Easy)

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?
'''

class Solution(object):
  def isPowerOfFour(self, num):
    if num <= 0:
      return False
    result = (num&(num-1) == 0) # power of two
    result = result and (num%3==1)
    return result


if __name__ == '__main__':
  a = Solution()
  print a.isPowerOfFour(2)
