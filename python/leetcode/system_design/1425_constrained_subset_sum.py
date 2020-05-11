"""
1425. Constrained Subset Sum (Hard)

Given an integer array nums and an integer k, return the maximum sum of a non-empty subset of that array such that for every two consecutive integers in the subset, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.

A subset of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.

 

Example 1:

Input: nums = [10,2,-10,5,20], k = 2
Output: 37
Explanation: The subset is [10, 2, 5, 20].
Example 2:

Input: nums = [-1,-2,-3], k = 1
Output: -1
Explanation: The subset must be non-empty, so we choose the largest number.
Example 3:

Input: nums = [10,-2,-10,-5,20], k = 2
Output: 23
Explanation: The subset is [10, -2, -5, 20].
 

Constraints:

1 <= k <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
"""

import collections
import heapq


class Solution(object):
    def constrainedSubsetSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # too slow!
        # O(n logk)
        memo = collections.deque()
        q = []
        res = min(nums)
        for i, item in enumerate(nums):
            if i == 0:
                memo.append(item)
                q.append(-item)
            else:
                # remove if necessary
                if len(memo) == k + 1:
                    tmp = memo.popleft()
                    q.remove(-tmp)
                    heapq.heapify(q)
                # print('before', memo, q, item)

                tmp_res = max(0, -q[0]) + item
                memo.append(tmp_res)
                heapq.heappush(q, -tmp_res)
            res = max(res, -q[0])
            # print('after', memo, q)
        return res


    def solve2(self, nums, k):
        # memo[i]: keeps result with nums[i] as last item
        # decreasing queue:
        memo = []
        q = collections.deque([])
        final = min(nums)
        for i, item in enumerate(nums):
            # remove window out of size k
            while len(q) > 0 and q[0][1] <= i-k-1:
                _ = q.popleft()
            # print('q', q)
            res = item
            if len(q) > 0:
                res = max(q[0][0] + item, res)
            while len(q) > 0 and res >= q[-1][0]:
                _ = q.pop()
            memo.append(res)
            q.append((res, i))
            # print(item, memo)
            final = max(final, res)
        return final


if __name__ == "__main__":
    a = Solution()
    assert a.solve2([10,2,-10,5,20], 2) == 37
    assert a.solve2([-1,-2,-3], 1) == -1
    assert a.solve2([10,-2,-10,-5,20], 2) == 23
