'''
146. LRU Cache (Medium)

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.last = None
        self.next = None

class DList(object):
    def __init__(self):
        self.head = None # head: most recent
        self.tail = None # tail
        self.n = 0

    def appendleft(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.last = node
            self.head = node
        self.n += 1

    def move_front(self, node):
        # move a node to head given that node
        if node is self.head:
            return
        # if self.tail is node:
        last_ = node.last
        next_ = node.next
        last_.next = next_
        if next_:
            next_.last = last_
        else: # node is tail
            self.tail = last_
        node.next = self.head
        self.head.last = node
        self.head = node

    def remove_tail(self):
        # remove a node given to the point to that node
        k, _ = self.tail.val
        if self.n == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.last
            self.tail.next = None
        self.n -= 1
        return k

    def print_l(self):
        n = self.head
        res = []
        while n is not None:
            res.append(n.val)
            if n.next is not None:
                assert n.next.last == n
            n = n.next
        print(res)


# from collections import deque


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dlist = DList()
        self.memo = {} # key to node
        self.c = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # get node
        if key not in self.memo:
            return -1
        else:
            node = self.memo[key]
            _, v = node.val
            self.dlist.move_front(node)
            return v

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.memo:
            node = self.memo[key]
            node.val = (key, value)
            self.dlist.move_front(node)
        else:
            node = Node((key, value))
            self.dlist.appendleft(node)
            self.memo[key] = node
            # remove lru
            if self.dlist.n > self.c:
                k = self.dlist.remove_tail()
                del self.memo[k]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
assert cache.get(1) == 1
cache.put(3, 3)
cache.dlist.print_l()
assert cache.get(2) == -1
cache.put(4, 4)
assert cache.get(1) == -1
assert cache.get(3) == 3
assert cache.get(4) == 4