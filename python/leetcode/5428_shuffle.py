class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i1, i2 in zip(nums[:n], nums[n:]):
            res.append(i1)
            res.append(i2)
        return res


if __name__ == "__main__":
    a = Solution()
    print(a.shuffle([2,5,1,3,4,7], 3))
