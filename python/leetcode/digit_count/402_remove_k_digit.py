"""
402. Remove K Digits (Medium)

Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be >= k.
The given num does not contain any leading zero.

Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
"""

class Solution(object):
  def removeKdigits(self, num, k):
    """
    :type num: str
    :type k: int
    :rtype: str
    """
    n = len(num)
    if k >= n: return '0'

    result = ''
    for i in range(n):
      if k == 0:
        result += num[i]
      elif len(result) == 0 or int(result[-1])<= int(num[i]):
        result += num[i]
      else:
        # remove until result is empty
        # or result
        while(k>0 and len(result)>0 and int(num[i])<int(result[-1])):
          result = result[:-1]
          k -= 1
        result += num[i]
      print 'step ', i, 'result', result, num
      # print result 

    # if k still >0
    if k>0:
      result = result[:-k]

    i = 0
    while(i<len(result) and result[i]=='0'):
      i += 1
    if i == len(result):
      result = '0'
    else:
      result = result[i:]
    return result


if __name__ == '__main__':
  a = Solution()
  # print a.removeKdigits("1432219", 3)
  # print a.removeKdigits("10200", 1)
  # print a.removeKdigits("10", 2)
  # print a.removeKdigits("10", 1)
  print a.removeKdigits("1234", 2)
