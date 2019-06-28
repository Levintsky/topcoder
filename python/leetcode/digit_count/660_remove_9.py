"""
660. Remove 9 (Hard)

Start from integer 1, remove any integer that contains 9 such as 9, 19, 29...

So now, you will have a new integer sequence: 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, ...

Given a positive integer n, you need to return the n-th integer after removing. Note that 1 will be the first integer.

Example 1:
Input: 9
Output: 10
Hint: n will not exceed 9 x 10^8.
"""

class Solution(object):
  def solve2(self, n):
    n_ = 0
    base = 1
    while n != 0:
      res = n % 9
      n_ += res * base
      base *= 10
      n /= 9
    return n_

  def newInteger(self, n):
    """
    :type n: int
    :rtype: int
    """
    if n < 9: return n
    n += 1

    cnt_9 = [0]
    for i in range(1, 11):
      tmp = self.count_k(i)
      tmp -= sum(cnt_9)
      cnt_9.append(tmp)
    print cnt_9
    cnt_no9 = [0]
    for i in range(1, 11):
      tmp = 9 * (10 ** (i-1))
      cnt_no9.append(tmp-cnt_9[i])
    cnt_no9[1] += 1
    print cnt_no9

    # step 2: solve the number
    i = 0
    while True:
      if n > cnt_no9[i]:
        n -= cnt_no9[i]
        i += 1
      else:
        print 'i-n:', i, n
        # solve the number (i-digit in total)
        result = 0
        for j in range(i, 0, -1): # solve the j-th digit
          print 'n', n, 'j', j
          if j != 1:
            digit = (n-1) / sum(cnt_no9[:j])
            print 'debug', j, n, cnt_no9[j-1]
            n = (n-1) % sum(cnt_no9[:j]) + 1
          else:
            digit = n - 1
          print 'digit', digit
          if j==i: digit += 1
          result += digit * (10**(j-1))
          print 'j', j, 'digit', digit, 'n', n
          print 'result', result
        return result
    

  def count_k(self, k):
    # how many k-digit with at least one 9
    # including starting with 0
    sign = 1
    result = 0
    for i in range(1, k+1):
      n = self.cki(k, i) * (10 ** (k-i))
      result += sign * n
      sign = -sign
    return result

  def cki(self, k, i):
    if i == k or i == 0:
      return 1
    elif i == k-1 or k == 1:
      return k
    else:
      return self.cki(k-1,i-1) + self.cki(k-1, i)


if __name__ == "__main__":
  a = Solution()
  # print 2000, a.newInteger(2000)
  print a.solve2(1234)
  # print 800000000, a.newInteger(800000000)
  '''
  print 2, a.newInteger(2)
  print 20, a.newInteger(20)
  print 200, a.newInteger(200)
  print 2000, a.newInteger(2000)
  print 800000000, a.newInteger(800000000)
  '''
