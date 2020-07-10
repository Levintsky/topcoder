class Solution(object):
    def getLastMoment(self, n, left, right):
        """
        :type n: int
        :type left: List[int]
        :type right: List[int]
        :rtype: int
        """
        res = 0
        if len(right) > 0:
            res = max(res, n-min(right))
        if len(left) > 0:
            res = max(res, max(left))
        return res


if __name__ == "__main__":
    a = Solution()
    print(a.getLastMoment(4, [4,3], [0,1]))
    print(a.getLastMoment(7, [], [0,1,2,3,4,5,6,7]))
    print(a.getLastMoment(7, [0,1,2,3,4,5,6,7], []))
    print(a.getLastMoment(9, [5], [4]))
    print(a.getLastMoment(6, [6], [0]))
