"""
1157. Online Majority Element In Subarray (Hard)

Implementing the class MajorityChecker, which has the following API:

MajorityChecker(int[] arr) constructs an instance of MajorityChecker with the given array arr;
int query(int left, int right, int threshold) has arguments such that:
0 <= left <= right < arr.length representing a subarray of arr;
2 * threshold > right - left + 1, ie. the threshold is always a strict majority of the length of the subarray
Each query(...) returns the element in arr[left], arr[left+1], ..., arr[right] that occurs at least threshold times, or -1 if no such element exists.

Example:

MajorityChecker majorityChecker = new MajorityChecker([1,1,2,2,1,1]);
majorityChecker.query(0,5,4); // returns 1
majorityChecker.query(0,3,3); // returns -1
majorityChecker.query(2,3,2); // returns 2
 

Constraints:

1 <= arr.length <= 20000
1 <= arr[i] <= 20000
For each query, 0 <= left <= right < len(arr)
For each query, 2 * threshold > right - left + 1
The number of queries is at most 10000
"""

import bisect

class MajorityChecker(object):

    def __init__(self, arr):
        """
        :type arr: List[int]
        """
        self.memo = {}
        for i, item in enumerate(arr):
            if item not in self.memo:
                self.memo[item] = []
            self.memo[item].append(i)
        

    def query(self, left, right, threshold):
        """
        :type left: int
        :type right: int
        :type threshold: int
        :rtype: int
        """
        for k in self.memo.keys():
            if len(self.memo[k]) < threshold:
                continue
            idx1 = bisect.bisect_left(self.memo[k], left)
            idx2 = bisect.bisect_left(self.memo[k], right)
            if idx2 == len(self.memo[k]) or self.memo[k][idx2] > right:
                idx2 -= 1
            if idx2 - idx1 + 1 >= threshold:
                return k
        return -1


if __name__ == "__main__":
    obj = MajorityChecker([1,1,2,2,1,1])
    print(obj.query(0,5,4))
    print(obj.query(0,3,3))
    print(obj.query(2,3,2))

# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)