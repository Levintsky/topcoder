class Solution(object):
    def circularPermutation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: List[int]
        """
        res = [0, 1]
        for i in range(1, n):
            newres = res[::-1]
            newres = [item + 2**i for item in newres]
            res = res + newres
        # print(res)
        id_ = res.index(start)
        # print(id_)
        newres = res[id_:] + res[:id_]
        return newres


if __name__ == "__main__":
    a = Solution()
    print(a.circularPermutation(2, 3))
    print(a.circularPermutation(3, 2))
    