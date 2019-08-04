"""
1146. Snapshot Array (Medium)

Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length.  Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id

Example 1:

Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation: 
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5

Constraints:

1 <= length <= 50000
At most 50000 calls will be made to set, snap, and get.
0 <= index < length
0 <= snap_id < (the total number of times we call snap())
0 <= val <= 10^9
"""

import bisect

class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.arr_t = []
        self.arr_v = []
        for i in range(length):
            self.arr_t.append([-1]) # (t, val)
            self.arr_v.append([0])
        self.tmpid = 0
        # self.memo = {}
        self.active_set = {} # indices

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        # self.arr[index] = val
        self.active_set[index] = val

    def snap(self):
        """
        :rtype: int
        """
        for k, v in self.active_set.items():
            self.arr_t[k].append(self.tmpid)
            self.arr_v[k].append(v)
        # self.memo[self.tmpid] = tuple(self.arr)
        self.tmpid += 1
        self.active_set = {}
        return self.tmpid - 1

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        # return self.memo[snap_id][index]
        # find first id < snap_id
        idx = bisect.bisect(self.arr_t[index], snap_id) - 1
        return self.arr_v[index][idx]


if __name__ == "__main__":
    a = SnapshotArray(3)
    print(a.set(0, 5))
    print(a.snap())
    print(a.set(0, 6))
    print(a.get(0, 0))
    print(a.set(1, 2))
    print(a.snap())
    print(a.get(1, 0))
    print(a.get(1, 1))
    print(a.get(0, 1))