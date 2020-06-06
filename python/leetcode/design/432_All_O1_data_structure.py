"""
432. All O`one Data Structure (Hard)

Implement a data structure supporting the following operations:

Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".
Challenge: Perform all these in O(1) time complexity.
"""


class AllOne(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = {}  # str 2 key
        self.rev_table = {}

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if key in self.table:
            self.table[key] += 1
        else:
            self.table[key] = 1
        tmp_v = self.table[key]
        if tmp_v == 1:
            if 1 not in self.rev_table:
                self.rev_table[1] = set([key])
            else:
                self.rev_table[1].add(key)
        else:
            self.rev_table[tmp_v - 1].remove(key)
            if tmp_v in self.rev_table:
                self.rev_table[tmp_v].add(key)
            else:
                self.rev_table[tmp_v] = set([key])
            if len(self.rev_table[tmp_v - 1]) == 0:
                del self.rev_table[tmp_v - 1]

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key not in self.table:
            return
        else:
            self.table[key] -= 1
            tmp_v = self.table[key]
            if tmp_v == 0:
                del self.table[key]
                self.rev_table[1].remove(key)
            else:
                self.rev_table[tmp_v + 1].remove(key)
                if tmp_v in self.rev_table:
                    self.rev_table[tmp_v].add(key)
                else:
                    self.rev_table[tmp_v] = set([key])
            if len(self.rev_table[tmp_v + 1]) == 0:
                del self.rev_table[tmp_v + 1]

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if len(self.rev_table) == 0:
            return ""
        v_max = max(self.rev_table.keys())
        x = self.rev_table[v_max].pop()
        self.rev_table[v_max].add(x)
        return x

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if len(self.rev_table) == 0:
            return ""
        v_min = min(self.rev_table.keys())
        x = self.rev_table[v_min].pop()
        self.rev_table[v_min].add(x)
        return x


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
