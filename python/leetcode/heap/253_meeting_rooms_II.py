"""
253. Meeting Rooms II (Medium)

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.
"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# from Queue import PriorityQueue
from heapq import *


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
    :type intervals: List[Interval]
    :rtype: int
    """
        ints = []
        for int_ in intervals:
            i, j = int_.start, int_.end
            ints.append((i, j))
        ints.sort()  # sort based on start

        heap = []
        result = 0
        for item in ints:
            start, end = item
            while len(heap) > 0 and heap[0] <= start:
                heappop(heap)
            heappush(heap, end)
            result = max(result, len(heap))
        return result
