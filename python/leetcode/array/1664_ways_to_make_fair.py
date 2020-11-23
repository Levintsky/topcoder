"""
1664. Ways to Make a Fair Array (Medium)

You are given an integer array nums. You can choose exactly one index (0-indexed) and remove the element. Notice that the index of the elements may change after the removal.

For example, if nums = [6,1,7,4,1]:

Choosing to remove index 1 results in nums = [6,7,4,1].
Choosing to remove index 2 results in nums = [6,1,4,1].
Choosing to remove index 4 results in nums = [6,1,7,4].
An array is fair if the sum of the odd-indexed values equals the sum of the even-indexed values.

Return the number of indices that you could choose such that after the removal, nums is fair.

 

Example 1:

Input: nums = [2,1,6,4]
Output: 1
Explanation:
Remove index 0: [1,6,4] -> Even sum: 1 + 4 = 5. Odd sum: 6. Not fair.
Remove index 1: [2,6,4] -> Even sum: 2 + 4 = 6. Odd sum: 6. Fair.
Remove index 2: [2,1,4] -> Even sum: 2 + 4 = 6. Odd sum: 1. Not fair.
Remove index 3: [2,1,6] -> Even sum: 2 + 6 = 8. Odd sum: 1. Not fair.
There is 1 index that you can remove to make nums fair.
Example 2:

Input: nums = [1,1,1]
Output: 3
Explanation: You can remove any index and the remaining array is fair.
Example 3:

Input: nums = [1,2,3]
Output: 0
Explanation: You cannot make a fair array after removing any index.
 

Constraints:

1 <= nums.length <= 10 ^ 5
1 <= nums[i] <= 10 ^ 4
"""

class Solution(object):
    def waysToMakeFair(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 1
        
        def get_presum(nums_):
            psum = nums_[:2]
            for item in nums_[2:]:
                psum.append(psum[-2] + item)
            return psum
            
        # forward
        presum = get_presum(nums)
        
        # postsum
        nums = nums[::-1]
        postsum = get_presum(nums)
        postsum = postsum[::-1]
        nums = nums[::-1]
        
        res = 0
        for i in range(n):
            # if delete i?
            # i-3, i-1, i+2, ... seq
            # presum[i-1] + postsum[i+2]
            sum1 = presum[i-1] if i > 0 else 0
            sum1 += postsum[i+2] if (i + 2) < n else 0
            
            # i-4, i-2, i+1
            sum2 = presum[i] - nums[i]
            sum2 += postsum[i+1] if (i + 1) < n else 0
            if sum1 == sum2:
                res += 1
        return res
        