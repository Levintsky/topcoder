"""
346. Moving Average from Data Stream (Easy)

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

For example,
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
"""

from collections import deque

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.q = deque()
        self.size = size
        self.accu = 0
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.q.append(val)
        self.accu += val
        if len(self.q) > self.size:
          item = self.q.popleft()
          self.accu -= item
        ret = float(self.accu) / len(self.q)
        return ret 


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

if __name__ == "__main__":
    obj = MovingAverage(3)
    print obj.next(1)
    print obj.next(10)
    print obj.next(3)
    print obj.next(5)
