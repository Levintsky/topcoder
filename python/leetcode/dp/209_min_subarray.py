'''
209. Minimum Size Subarray Sum (Medium)

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
'''

import collections

class Solution(object):
    def minSubArrayLen(self, s, nums):
        if len(nums) == 0:
            return 0
        st = 0
        end = 0
        n = len(nums)
        curr = nums[0]
        best = len(nums) + 1
        while(end<n):
            if curr>=s:
                while(curr-nums[st]>=s):
                    curr -= nums[st]
                    st += 1
                best = min(best, end-st+1)
                if best == 1:
                    return best
            end += 1
            if end != n:
                curr += nums[end]
        if best>len(nums):
            return 0
        else:
            return best

    def solve2(self, s, nums):
        q = collections.deque()
        q.append([0, -1])
        cumu = 0
        
        best = len(nums) + 1
        for i, item in enumerate(nums):
            cumu = cumu + item
            
            while len(q) > 0 and q[0][0] <= cumu - s:
                best = min(best, i-q[0][1])
                _ = q.popleft()
            q.append([cumu, i])
            
        if best <= len(nums):
            return best
        else:
            return 0

if __name__ == '__main__':
    a = Solution()
    print(a.minSubArrayLen(7, [2,3,1,2,4,3]))
    print(a.minSubArrayLen(5, [2,3,1,1,1,1,1]))
