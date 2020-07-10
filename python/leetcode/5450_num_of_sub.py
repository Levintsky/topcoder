class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        i, j = 0, len(nums) - 1
        res = 0
        mod = 10 ** 9 + 7
        while i <= j:
            if nums[i] + nums[j] > target:
                j -= 1
            else:
                res = (res + 2 ** (j - i)) % mod
                i += 1
        return res


if __name__ == "__main__":
    a = Solution()
    print(a.numSubseq([3,5,6,7], 9))
    print(a.numSubseq([3,3,6,8], 10))
    print(a.numSubseq([2,3,3,4,6,7], 12))
    print(a.numSubseq([5,2,4,1,7,6,8], 16))