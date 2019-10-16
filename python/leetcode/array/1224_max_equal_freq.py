"""
1224. Maximum Equal Frequency (Hard)

Given an array nums of positive integers, return the longest possible length of an array prefix of nums, such that it is possible to remove exactly one element from this prefix so that every number that has appeared in it will have the same number of occurrences.

If after removing one element there are no remaining elements, it's still considered that every appeared number has the same number of ocurrences (0).

Example 1:

Input: nums = [2,2,1,1,5,3,3,5]
Output: 7
Explanation: For the subarray [2,2,1,1,5,3,3] of length 7, if we remove nums[4]=5, we will get [2,2,1,1,3,3], so that each number will appear exactly twice.

Example 2:

Input: nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
Output: 13

Example 3:

Input: nums = [1,1,1,2,2,2]
Output: 5

Example 4:

Input: nums = [10,2,8,9,3,8,1,5,2,3,7,6]
Output: 8

Constraints:

2 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
"""

class Solution(object):
    def maxEqualFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        memo = {} # item -> occurrence
        memo_memo = {}
        for i, item in enumerate(nums):
        	memo[item] = memo.get(item, 0) + 1
        	if i == 0:
        		memo_memo[1] = 1
        	else:
        		# case 1: item never appears
        		if memo[item] == 1:
        			memo_memo[1] = memo_memo.get(1, 0) + 1
        		else:
        			old_cnt, new_cnt = memo[item]-1, memo[item]
        			memo_memo[old_cnt] -= 1
        			memo_memo[new_cnt] = memo_memo.get(new_cnt, 0) + 1
        			if memo_memo[old_cnt] == 0:
        				del memo_memo[old_cnt]
        	# print(i, memo_memo)
        	keys = memo_memo.keys()
        	min_key, max_key = min(keys), max(keys)
        	# case 1: [1,1,2,2,3,3,3] style
        	if min_key == max_key - 1 and memo_memo[max_key] == 1:
        		result = i + 1
        	# case 2: [1,1,2,2,3,3,k] style
        	if min_key == max_key and i != len(nums)-1:
        		result = i + 2
        	# case 3:
        	if min_key == 1 and memo_memo[1] == 1 and len(keys) == 2:
        		result = i + 1
        return result


if __name__ == "__main__":
	a = Solution()
	print(a.maxEqualFreq([1,1,1,2,2,2,3,3,3,4,4,4,5]))
	print(a.maxEqualFreq([1,1,1,2,2,2]))
	print(a.maxEqualFreq([10,2,8,9,3,8,1,5,2,3,7,6]))
	print(a.maxEqualFreq([2,2,1,1,5,3,3,5]))