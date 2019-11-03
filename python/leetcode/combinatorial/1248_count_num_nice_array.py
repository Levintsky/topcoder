"""
1248. Count Number of Nice Subarrays

Given an array of integers nums and an integer k. A subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
 

Constraints:

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length
"""

class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        stat = [0]
        for item in nums:
        	if item % 2 == 0:
        		stat[-1] += 1
        	else:
        		stat.append(0)
        res = 0
        # if k == 1:
        # 	return sum(stat)
        for i in range(k, len(stat)):
        	res += (stat[i]+1) * (stat[i-k]+1)
        return res


if __name__ == "__main__":
	a = Solution()
	print(a.numberOfSubarrays([1,1,2,1,1], 3))
	print(a.numberOfSubarrays([2,4,6], 1))
	print(a.numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2))