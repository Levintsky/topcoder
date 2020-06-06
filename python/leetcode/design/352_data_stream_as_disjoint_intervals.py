'''
352. Data Stream as Disjoint Intervals (Hard)

Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize the numbers seen so far as a list of disjoint intervals.

For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary will be:

[1, 1]
[1, 1], [3, 3]
[1, 1], [3, 3], [7, 7]
[1, 3], [7, 7]
[1, 3], [6, 7]
Follow up:
What if there are lots of merges and the number of disjoint intervals are small compared to the data stream's size?
'''

"""
Java: TreeMap

Use TreeMap to easily find the lower and higher keys, the key is the start of the interval.
Merge the lower and higher intervals when necessary. The time complexity for adding is O(logN) since lowerKey(), higherKey(), put() and remove() are all O(logN). It would be O(N) if you use an ArrayList and remove an interval from it.

public class SummaryRanges {
    TreeMap<Integer, Interval> tree;

    public SummaryRanges() {
        tree = new TreeMap<>();
    }

    public void addNum(int val) {
        if(tree.containsKey(val)) return;
        Integer l = tree.lowerKey(val);
        Integer h = tree.higherKey(val);
        if(l != null && h != null && tree.get(l).end + 1 == val && h == val + 1) {
            tree.get(l).end = tree.get(h).end;
            tree.remove(h);
        } else if(l != null && tree.get(l).end + 1 >= val) {
            tree.get(l).end = Math.max(tree.get(l).end, val);
        } else if(h != null && h == val + 1) {
            tree.put(val, new Interval(val, tree.get(h).end));
            tree.remove(h);
        } else {
            tree.put(val, new Interval(val, val));
        }
    }

    public List<Interval> getIntervals() {
        return new ArrayList<>(tree.values());
    }
}
"""

import heapq 

# Definition for an interval.
class Interval(object):
  def __init__(self, s=0, e=0):
    self.start = s
    self.end = e

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # priority queue: tuple(val, Interval(begin, end))
        self.intervals = [] 


    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        heapq.heappush(self.intervals, (val, Interval(val, val)))
        

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        stack = []
        while len(self.intervals) > 0:
          idx, intv = heapq.heappop(self.intervals)
          if not stack:
            stack.append((idx, intv))
          else:
            _, prev = stack[-1]
            if prev.end + 1 >= intv.start:
              prev.end = max(prev.end, intv.end)
            else:
              stack.append((idx, intv))
        self.intervals = stack
        return list(map(lambda x: x[1], stack))

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
def print_func(result):
  print 'print result:'
  for item in result:
    print item.start, item.end

if __name__ == "__main__":
  a = SummaryRanges()
  a.addNum(1)
  result = a.getIntervals()
  print_func(result)

  a.addNum(3)
  result = a.getIntervals()
  print_func(result)

  a.addNum(7)
  result = a.getIntervals()
  print_func(result)

  a.addNum(2)
  result = a.getIntervals()
  print_func(result)
