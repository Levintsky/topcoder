'''
31. Next Permutation (Medium)

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 to 1,3,2
3,2,1 to 1,2,3
1,1,5 to 1,5,1
'''

"""
key points:
1. from back to front;
2. switch and re-order
3. do it in-order, i.e., nums = nums[::-1] is not ok.
"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # remember the [2,3,1] case!!
        n = len(nums)
        if n <= 1: return
        
        i = n - 1
        while i > 0:
            if nums[i-1] < nums[i]:
                break
            i -= 1
        if i == 0:
            i, j = 0, n - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i+1, j-1
            print nums
            return
        else:
            i -= 1
            j = i + 1
            while j < n and nums[j] > nums[i]:
                j += 1
            j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            nums[i+1:n] = nums[n-1:i:-1]
            print nums


if __name__ == "__main__":
    a = Solution()
    print a.nextPermutation([1,2,3]) 
    print a.nextPermutation([3,2,1]) 
    print a.nextPermutation([1,1,5]) 
    print a.nextPermutation([3,8,3,2,1]) 
