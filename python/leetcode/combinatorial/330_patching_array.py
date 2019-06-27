"""
330. Patching Array (Hard)

Given a sorted positive integer array nums and an integer n, add/patch elements to the array such that any number in range [1, n] inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches required.

Example 1:
nums = [1, 3], n = 6
Return 1.

Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.

Example 2:
nums = [1, 5, 10], n = 20
Return 2.
The two patches can be [2, 4].

Example 3:
nums = [1, 2, 2], n = 5
Return 0.
"""

"""
Keypoints: no need to enumerate n+1, if n exists,
  since 1 should have been added if not appearing.

Let miss be the smallest sum in [0,n] that we might be missing. 
Meaning we already know we can build all sums in [0,miss). 
Then if we have a number num <= miss in the given array, 
  we can add it to those smaller sums to build all sums in [0,miss+num).
If we don't, then we must add such a number to the array,
  and it's best to add miss itself, to maximize the reach.

missing: least potential missing number, i.e.,
  we can build [0, missing)
if next number num[i] <= missing;
  we can build [0, missing + num[i])
else:
  add missing,
  missing *= 2
"""

from collections import Counter


class Solution(object):
    def minPatches(self, nums, n):
        """
    :type nums: List[int]
    :type n: int
    :rtype: int
    """

    def solve2(self, nums, n):
        if n == 0:
            return 0
        nums.sort()
        miss = 1
        i = 0
        result = 0
        while miss <= n:
            # it is not a miss, add all possible
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:  # add miss into the system
                result += 1
                miss *= 2
        return result


if __name__ == "__main__":
    a = Solution()
    # print a.minPatches([1,3], 6)
    print(a.solve2([1, 3], 6))
    # print a.minPatches([1,5,10], 20)
    print(a.solve2([1, 5, 10], 20))
    # print a.minPatches([1,2,2], 5)
    print(a.solve2([1, 2, 2], 5))
    # print a.minPatches([1,2,31,33], 1000)
    print(a.solve2([1, 2, 31, 33], 1000))
    # print a.minPatches([1,2,31,33], 2147483647)
    print(a.solve2([1, 2, 31, 33], 2147483647))
