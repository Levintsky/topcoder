"""
1512. Number of Good Pairs (Easy)

Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""

class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        memo = [0] * k
        for item in arr:
            it = item % k
            memo[it] += 1

        for i in range(1, k):
            if memo[i] != memo[k-i]:
                return False
        if k % 2 == 0 and memo[k//2] % 2 == 1:
            return False
        return True


if __name__ == "__main__":
    a = Solution()
    print(a.canArrange([1,2,3,4,5,10,6,7,8,9], 5))
    print(a.canArrange([1,2,3,4,5,6], 7))
    print(a.canArrange([1,2,3,4,5,6], 10))
    print(a.canArrange([-10,10], 2))
    print(a.canArrange([-1,1,-2,2,-3,3,-4,4], 3))