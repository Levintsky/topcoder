"""
526. Beautiful Arrangement (Medium)

Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:

The number at the ith position is divisible by i.
i is divisible by the number at the ith position.
Now given N, how many beautiful arrangements can you construct?

Example 1:
Input: 2
Output: 2
Explanation: 

The first beautiful arrangement is [1, 2]:

Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

The second beautiful arrangement is [2, 1]:

Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.

Note:
N is a positive integer and will not exceed 15.
"""

class Solution(object):
  def solve(self, N):
    tmp_list = [0]*N
    cnt = 0
    tmp_set = set()
    cnt = self.recur(tmp_list, 0, N, cnt, tmp_set)
    return cnt 

  def recur(self, tmp_list, i, N, cnt, tmp_set):
    # i-th position
    for tmp in range(1, N+1):
      # print tmp, tmp_set, tmp not in tmp_set
      if (tmp not in tmp_set) and (tmp % (i+1) == 0 or (i+1) % tmp == 0):
        tmp_list[i] = tmp
        tmp_set.add(tmp)
        # print tmp, tmp_set, tmp_list
        if i == N-1:
          # print tmp_list
          cnt += 1
        else:
          cnt = self.recur(tmp_list, i+1, N, cnt, tmp_set)
        tmp_set.remove(tmp)
    return cnt

  def countArrangement(self, N):
    """
    :type N: int
    :rtype: int
    """
    if N == 1: return 1
    result = [[1,2],[2,1]]

    for i in range(3, N+1):
      new_result = []
      for tmp_list in result:
        # print 'old', tmp_list
        new_list = tmp_list + [i]
        # print 'new', new_list
        new_result.append(new_list)
        for j in range(len(tmp_list)):
          if i % tmp_list[j] == 0 and i % (j+1)==0:
            new_list = tmp_list + [i]
            new_list[-1], new_list[j] = new_list[j], new_list[-1]
            # print 'new', new_list
            new_result.append(new_list)
      result = new_result
      print result
    return len(result)


if __name__ == '__main__':
  a = Solution()
  print a.solve(10)
  # print a.countArrangement(6)

