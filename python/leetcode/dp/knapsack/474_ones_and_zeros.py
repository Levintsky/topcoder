'''
474. Ones and Zeroes (Medium)

In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.

For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, there is an array with strings consisting of only 0s and 1s.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

Note:
The given numbers of 0s and 1s will both not exceed 100
The size of given string array won't exceed 600.
Example 1:
Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
Output: 4

Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are "10","0001","1","0"

Example 2:
Input: Array = {"10", "0", "1"}, m = 1, n = 1
Output: 2

Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".
'''

"""
0-1 Knapsack problem
time complexity: O(m*n*len(strs))

a matrix m by n to remember best solution with k strs(dp)
iterate over the strings
"""
import collections

class Solution(object):
  def findMaxForm(self, strs, m, n):
    """
    :type strs: List[str]
    :type m: int
    :type n: int
    :rtype: int
    """
    n_strs = len(strs)

    strs_cnt = []
    for item in strs:
      strs_cnt.append(self.count_0_1(item))
    print strs_cnt

    # create a [m,n] matrix
    matrix = []
    for i in range(m+1):
      tmp = [0] * (n+1)
      matrix.append(tmp)
    print matrix

    # dp
    for i in range(n_strs):
      # update matrix
      mi, ni = strs_cnt[i]
      for mm in range(m,-1,-1):
        for nn in range(n,-1,-1):
          if mm-mi>=0 and nn-ni>=0:
            matrix[mm][nn] = max(matrix[mm][nn], matrix[mm-mi][nn-ni]+1)
      print matrix
    return matrix[-1][-1]

  def count_0_1(self, tmp_str):
    cnt0, cnt1 = 0, 0
    i = 0
    while(i<len(tmp_str)):
      tmp = tmp_str[i]
      if tmp == '0': cnt0 += 1
      else: cnt1 += 1
      i += 1
    return (cnt0, cnt1)


if __name__ == '__main__':
  a = Solution()
  print a.findMaxForm(["10", "0001", "111001", "1", "0"], 5,3)
  print a.findMaxForm(["10", "1", "0"], 1,1)
