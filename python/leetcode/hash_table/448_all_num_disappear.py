'''
448. Find All Numbers Disappeared in an Array (Easy)

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''


class Solution(object):
    def findDisappear(self, nums):
        # put everything into a set
        num_set = set(nums)
        all_set = set(range(1, len(nums)+1))
        dis_set = all_set - num_set
        return list(dis_set)

    def solve2(self, nums):
        n = len(nums)
        for i in range(n):
            if nums[i] == -1:
                continue
            j = nums[i]
            while j != -1:
                k = nums[j-1]
                nums[j-1], j = -1, k
        res = []
        for i, item in enumerate(nums):
            if item != -1:
                res.append(i+1)
        return res


if __name__ == '__main__':
    a = Solution()
    print(a.findDisappear([4,3,2,7,8,2,3,1]))
    print(a.findDisappear([1,1]))
