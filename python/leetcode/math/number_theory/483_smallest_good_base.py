"""
483. Smallest Good Base (Hard)

For an integer n, we call k>=2 a good base of n, if all digits of n base k are 1.

Now given a string representing n, you should return the smallest good base of n in string format. 

Example 1:
Input: "13"
Output: "3"
Explanation: 13 base 3 is 111.

Example 2:
Input: "4681"
Output: "8"
Explanation: 4681 base 8 is 11111.

Example 3:
Input: "1000000000000000000"
Output: "999999999999999999"
Explanation: 1000000000000000000 base 999999999999999999 is 11.

Note:
The range of n is [3, 10^18].
The string representing n is always valid and will not have leading zeros.
"""
import math

class Solution(object):
  def smallestGoodBase(self, n):
    """
    :type n: str
    :rtype: str
    """
    if n == 1: return 2
    k = int(math.ceil(math.log(n,2))) # will not be more than 1111..1
    for i in range(k, 1, -1):
      if i == 2: return n-1
      # try to get 1111 (k)
      min_ = int(math.ceil(math.pow(n/2, 1./float(i-1)))) 
      max_ = int(math.ceil(math.pow(n, 1./float(i-1))))
      print 'search', i, min_, max_
      # binary search
      start = min_
      end = max_ + 1
      while start <= end:
        mid = (start+end)/2
        tmp = self.helper(mid,i)
        print mid, i, tmp
        if tmp == n: return mid
        elif tmp > n: end = mid -1
        else: start = mid + 1
    return n-1

  def helper(self, base, k):
    cnt = 0
    for i in range(k):
      cnt += base**i
    return cnt


if __name__ == '__main__':
  a = Solution()
  print a.smallestGoodBase(13) 
  print a.smallestGoodBase(3541) 
