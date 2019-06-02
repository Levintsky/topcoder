"""
1063. Number of Valid Subarrays (Hard)

Given an array A of integers, return the number of non-empty continuous subarrays that satisfy the following condition:

The leftmost element of the subarray is not larger than other elements in the subarray.

Example 1:

Input: [1,4,2,5,3]
Output: 11
Explanation: There are 11 valid subarrays: [1],[4],[2],[5],[3],[1,4],[2,5],[1,4,2],[2,5,3],[1,4,2,5],[1,4,2,5,3].
Example 2:

Input: [3,2,1]
Output: 3
Explanation: The 3 valid subarrays are: [3],[2],[1].
Example 3:

Input: [2,2,2]
Output: 6
Explanation: There are 6 valid subarrays: [2],[2],[2],[2,2],[2,2],[2,2,2].

Note:

1 <= A.length <= 50000
0 <= A[i] <= 100000
"""

"""
Solution 1:
heapq: O(nlogn)

Solution 2:
"""

import heapq

class Solution(object):
    def validSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        q = []
        for item in nums:
            while len(q) > 0 and q[0] < -item:
                _ = heapq.heappop(q)
            heapq.heappush(q, -item)
            res += len(q)
        return res

    def solve2(self, nums):
        res = 0
        stack = []
        for item in nums:
            while len(stack) > 0 and item < stack[-1]:
                _ = stack.pop()
            stack.append(item)
            res += len(stack)
            print(item, stack, res)
        return res


if __name__ == "__main__":
    a = Solution()
    # print(a.validSubarrays([1,4,2,5,3]))
    # print(a.validSubarrays([3,2,1]))
    # print(a.validSubarrays([2,2,2]))
    print(a.solve2([1,4,2,5,3]))
