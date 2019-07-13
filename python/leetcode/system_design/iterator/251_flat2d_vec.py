"""
251. Flatten 2D Vector (Medium)

Implement an iterator to flatten a 2d vector.

For example,
Given 2d vector =

[
  [1,2],
  [3],
  [4,5,6]
]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].

Follow up:
As an added challenge, try to code it using only iterators in C++ or iterators in Java.
"""

class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.data = vec2d
        self.idx = None

    def next(self):
        """
        :rtype: int
        """
        i, j = self.idx
        return self.data[i][j]

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.data) == 0:
          return False
        if self.idx is None:
          self.idx = [0, 0]
        else:
          i, j = self.idx
          j += 1
          self.idx = [i, j]

        i, j = self.idx
        # get to the next index return True
        if j < len(self.data[i]):
          return True

        i, j = i+1, 0
        while i != len(self.data):
          if len(self.data[i]) > 0:
            self.idx = [i, j]
            return True
          else:
            i, j = i+1, 0
        return False


class Vector2D2(object):
    def __init__(self, vec2d):
        self.data = vec2d
        self.total = 0
        self.idx2d = None
        for i in range(len(vec2d)):
            self.total += len(vec2d[i])
            if self.idx2d is None and len(vec2d[i]) > 0:
                self.idx2d = (i, 0)
        self.idx1d = 0

    def next(self):
        i, j = self.idx2d
        item = self.data[i][j]
        # go to next
        if j != len(self.data[i]) - 1:
            j += 1
            self.idx2d = (i, j)
        else:
            for j in range(i+1, len(self.data)):
                if len(self.data[j]) > 0:
                    self.idx2d = (j, 0)
                    break
        self.idx1d += 1
        return item

    def hasNext(self):
        print(self.idx1d, self.total)
        return not self.idx1d == self.total

    def reset(self):
        self.idx2d = None
        for i in range(len(self.data)):
            if self.idx2d is None and len(self.data[i]) > 0:
                self.idx2d = (i, 0)
        self.idx1d = 0

    def removeSelf(self):
        i, j = self.idx2d
        self.data[i].pop(j)
        self.total -= 1
        # already at the end, no need to check next valid
        if self.total == self.idx1d:
            return
        if j == len(self.data[i]):
            for ii in range(i+1, len(self.data)):
                if len(self.data) > 0:
                    self.idx2d = ii, 0
                    break

if __name__ == "__main__":
    vec = [[1,2], [3], [4]]
    iterator = Vector2D2(vec)
    for i in range(3):
        print(iterator.next())
    print(iterator.hasNext())
    print(iterator.next())
    print(iterator.hasNext())
    iterator.reset()
    for i in range(4):
        if i % 2 == 0:
            iterator.removeSelf()
        else:
            _ = iterator.next()
        print(iterator.data, iterator.idx2d, iterator.idx1d)
    # print(iterator.data)
    """
    while i.hasNext():
        v.append(i.next())
        print(v)
    """
# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
