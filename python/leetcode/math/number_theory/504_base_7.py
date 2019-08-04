'''
504. Base 7 (Easy)

Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
Note: The input will be in range of [-1e7, 1e7].
'''


class Solution(object):
  def convertToBase7(self, num):
    """
    :type num: int
    :rtype: str
    """
    # AC, original solution
    if num > 0:
      result = ''
      while(num>0):
        rem = num % 7
        result += str(rem)
        num = num // 7
      result = result[::-1]
      return result
    elif num == 0:
      return '0'
    else: # negative
      result = ''
      while(num<0):
        rem = num%7
        if rem == 0:
          result += str(rem)
          num = num // 7
        else:
          rem = 7 - rem
          result += str(rem)
          num = num // 7 + 1
      result = result[::-1]
      result = '-'+result
      return result

  def solution2(self, num):
    # AC, better solution
    if num == 0: return '0'
    neg_flag = num < 0
    num = abs(num)
    result = ''
    while(num>0):
      result += str(num % 7)
      num /= 7
    result = result[::-1]
    if neg_flag: result = '-'+result
    return result

if __name__ == '__main__':
  a = Solution()
  print a.convertToBase7(100)
  print a.solution2(100)
  print a.convertToBase7(0)
  print a.solution2(0)
  print a.convertToBase7(-100)
  print a.solution2(-100)
