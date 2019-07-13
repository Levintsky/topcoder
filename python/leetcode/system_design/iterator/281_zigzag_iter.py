"""
281. Zigzag Iterator (Medium)

Given two 1d vectors, implement an iterator to return their elements alternately.

For example, given two 1d vectors:

v1 = [1, 2]
v2 = [3, 4, 5, 6]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].

Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?

Clarification for the follow up question - Update (2015-09-18):
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example, given the following input:

[1,2,3]
[4,5,6,7]
[8,9]
It should return [1,4,8,2,5,9,3,6,7].
"""

class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v = [v1, v2]
        self.ids = [0, 0]
        self.idx = 0 

    def next(self):
        """
        :rtype: int
        """
        curr_list = self.v[self.idx]
        if self.ids[self.idx] < len(curr_list):
          tmp = curr_list[self.ids[self.idx]]
          self.ids[self.idx] += 1
          self.idx = 1 - self.idx
          return tmp
        else:
          self.idx = 1 - self.idx
          curr_list = self.v[self.idx]
          tmp = curr_list[self.ids[self.idx]]
          self.ids[self.idx] += 1
          return tmp

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.ids[0] == len(self.v[0]) and self.ids[1] == len(self.v[1]):
          return False
        return True 
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())

v2 = []
v1 = [3,4,5,6]
i, v = ZigzagIterator(v1, v2), []
while i.hasNext():
  v.append(i.next())
  print v
