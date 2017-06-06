'''
435. Non-overlapping Intervals (Medium)

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note:
You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
Example 1:
Input: [ [1,2], [2,3], [3,4], [1,3] ]

Output: 1

Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:
Input: [ [1,2], [1,2], [1,2] ]

Output: 2

Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:
Input: [ [1,2], [2,3] ]

Output: 0

Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
'''

# Definition for an interval.
class Interval(object):
  def __init__(self, s=0, e=0):
    self.start = s
    self.end = e

class Solution(object):
  def eraseOverlapIntervals(self, intervals):
    """
    :type intervals: List[Interval]
    :rtype: int
    """
    return None

  def solution2(self, intervals):
    intervals.sort(key = lambda interval: (interval.start, interval.end))
    last = None
    remove = 0
    for curr in intervals:
      if last is None: last = curr
      else:
        if curr.start < last.end:
          # intersect decide which to remove
          if curr.end < last.end:
            last = curr
          remove += 1
        else:
          # keep it and update
          last = curr
    return remove

if __name__ == '__main__':
  int_list = [[0,2],[1,3],[1,3],[2,4],[3,5],[3,5],[4,6]]
  intervals = []
  for s,e in int_list:
    intervals.append(Interval(s,e))
  a = Solution()
  # print a.eraseOverlapIntervals([int1,int2])
  print a.solution2(intervals)
