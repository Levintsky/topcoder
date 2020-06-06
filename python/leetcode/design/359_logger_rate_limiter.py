"""
359. Logger Rate Limiter (Easy)

Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not printed in the last 10 seconds.

Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.

It is possible that several messages arrive roughly at the same time.

Example:

Logger logger = new Logger();

// logging string "foo" at timestamp 1
logger.shouldPrintMessage(1, "foo"); returns true; 

// logging string "bar" at timestamp 2
logger.shouldPrintMessage(2,"bar"); returns true;

// logging string "foo" at timestamp 3
logger.shouldPrintMessage(3,"foo"); returns false;

// logging string "bar" at timestamp 8
logger.shouldPrintMessage(8,"bar"); returns false;

// logging string "foo" at timestamp 10
logger.shouldPrintMessage(10,"foo"); returns false;

// logging string "foo" at timestamp 11
logger.shouldPrintMessage(11,"foo"); returns true;
"""

import heapq

class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []
        self.visited = set()

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        while len(self.q) > 0 and self.q[0][0] <= timestamp - 10:
          t, msg = heapq.heappop(self.q)
          self.visited.remove(msg)

        if message not in self.visited:
          heapq.heappush(self.q, (timestamp, message))
          self.visited.add(message)
          return True
        else:
          return False
        
from collections import defaultdict
class Solution(object):
    # Solution 2: faster
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = defaultdict(lambda: -1<<16)
        

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        recent = self.m[message]
        if timestamp - recent >= 10:
            self.m[message] = timestamp
        return (timestamp - recent) >= 10

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
if __name__ == "__main__":
    obj = Logger()
    print obj.shouldPrintMessage(1, "foo")
    print obj.shouldPrintMessage(2, "bar")
    print obj.shouldPrintMessage(3, "foo")
    print obj.shouldPrintMessage(8, "bar")
    print obj.shouldPrintMessage(10, "foo")
    print obj.shouldPrintMessage(11, "foo")
