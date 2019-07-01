"""
341. Flatten Nested List Iterator (Medium)

Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Example 2:
Given the list [1,[4,[6]]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.data = []
        for item in nestedList:
            self.append_data(item)
        self.i = 0
        self.n = len(self.data)

    def append_data(self, item):
        if item.isInteger():
            self.data.append(item.getInteger())
        else:
            sub_items = item.getList()
            for subitem in sub_items:
                self.append_data(subitem)

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            i = self.i
            self.i += 1
            return self.data[i]

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.i == self.n:
            return False
        else:
            return True


class NestedInteger(object):
    def __init__(self, data):
        self.data = data

    def isInteger(self):
        return isinstance(self.data, int)

    def getInteger(self):
        return self.data

    def getList(self):
        data = []
        for item in self.data:
            data.append(NestedInteger(item))
        return data

    def __len__(self):
        if self.isInteger():
            return 1
        else:
            return len(self.data)

    def __getitem__(self, index):
        return NestedInteger(self.data[index])


class NestedIterator2(object):

    def __init__(self, nestedList):
        self.stack = [[nestedList, 0]]

    def next(self):
        self.hasNext()
        nestedList, i = self.stack[-1]
        self.stack[-1][1] += 1
        return nestedList[i].getInteger()
            
    def hasNext(self):
        s = self.stack
        while s:
            nestedList, i = s[-1]
            if i == len(nestedList):
                s.pop()
            else:
                x = nestedList[i]
                if x.isInteger():
                    return True
                s[-1][1] += 1
                s.append([x.getList(), 0])
        return False
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

class NestedIterator4(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        from collections import deque
        self.nestedList = deque(nestedList)
        self.q = deque()

    def next(self):
        """
        :rtype: int
        """
        return self.q.popleft()

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.q: return True
        if not self.nestedList: return False
        while self.nestedList and not self.q:
            item = self.nestedList.popleft()
            if item.isInteger():
                self.q.append(item.getInteger())
            else:
                self.q.extend(self.flatten_list(item.getList()))
        if self.q:
            return True
        return False
    
    def flatten_list(self, intOrList):
        res = []
        for item in intOrList:
            if item.isInteger():
                res.append(item.getInteger())
            else:
                res.extend(self.flatten_list(item.getList()))
        return res

if __name__ == "__main__":
    data = NestedInteger([[1,1],2,[1,1]])
    i = NestedIterator2(data)
    while i.hasNext():
        print(i.next())