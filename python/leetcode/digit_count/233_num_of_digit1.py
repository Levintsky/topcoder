'''
233. Number of Digit One (Hard)

Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
'''

class Solution(object):
  def solve2(self, n):
    cnt = 0
    i = 1
    while i <= n:
      divider = i * 10
      cnt += (n / divider) * i
      cnt += min(max(n % divider - i + 1, 0), i)
      i *= 10
    return cnt
    
  def countDigitOne(self, n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 0: return 0

    # step 0: how many digits in n first
    n_list = []
    tmp = n
    while tmp != 0:
      n_list.append(tmp % 10)
      tmp /= 10
    print n_list
    cnt = len(n_list)

    # step 1: how many number with 1
    # stat[k]: for many for a k-digit
    stat = [0]
    for i in range(1, cnt):
      tmp = 1 * (10**(i-1)) + 9 * sum(stat)
      stat.append(tmp)
    print stat

    accu = []
    for i in range(len(stat)):
      accu.append(sum(stat[:i+1]))
    print accu

    # step 2: count it
    result = 0
    i = len(n_list) - 1
    while i >= 0:
      if i == 0:
        if n_list[i] >= 1:
          result += 1
          print 'add', 1
        break
      if n_list[i] > 0: # 0xxx
        result += accu[i]
      if n_list[i] == 1: # 1xx: all count
        tmp = 0
        j = i-1
        while j >= 0:
          tmp = tmp * 10 + n_list[j]
          j -= 1
        result += tmp+1
        print 'add', tmp+1
      elif n_list[i] > 1:
        # add 1xx
        result +=  10 ** i
        result += accu[i]
        result += (n_list[i]-2) * accu[i]
        # print 'add: ', 10 ** i+sum(stat[:i+1])+(n_list[i]-2) * stat[i]
      print i, result
      i -= 1
    return result


if __name__ == "__main__":
  a = Solution()
  print a.countDigitOne(13)
