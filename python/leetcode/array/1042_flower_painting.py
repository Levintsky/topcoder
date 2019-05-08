"""
1042. Flower Planting With No Adjacent (Easy)

You have N gardens, labelled 1 to N.  In each garden, you want to plant one 
of 4 types of flowers.

paths[i] = [x, y] describes the existence of a bidirectional path from 
garden x to garden y.

Also, there is no garden that has more than 3 paths coming into or leaving it.

Your task is to choose a flower type for each garden such that, for any two 
gardens connected by a path, they have different types of flowers.

Return any such a choice as an array answer, where answer[i] is the type 
of flower planted in the (i+1)-th garden.  The flower types are denoted 1, 2, 
3, or 4.  It is guaranteed an answer exists.

Example 1:

Input: N = 3, paths = [[1,2],[2,3],[3,1]]
Output: [1,2,3]
Example 2:

Input: N = 4, paths = [[1,2],[3,4]]
Output: [1,2,1,2]
Example 3:

Input: N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
Output: [1,2,3,4]

Note:

1 <= N <= 10000
0 <= paths.size <= 20000
No garden has 4 or more paths coming into or leaving it.
It is guaranteed an answer exists.
"""


class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        # memo: i to j
        memo = {}
        for i, j in paths:
            if i in memo:
                memo[i].append(j)
            else:
                memo[i]=[j]
            if j in memo:
                memo[j].append(i)
            else:
                memo[j]=[i]
        # dfs
        result = [-1] * N
        flag = False
        def dfs(idx):
            avail = set([1,2,3,4])
            if idx in memo:
                for idx2 in memo[idx]:
                    color = result[idx2-1]
                    if color in avail:
                        avail.remove(color)
            for c in avail:
                result[idx-1] = c
                if idx == N: return True
                else:
                    flag = dfs(idx+1)
                    if flag: return True
            return False
        dfs(1)
        return result

    def solve2(self, N, paths):
        res = [0] * N
        G = [[] for i in range(N)]
        for x, y in paths:
            G[x - 1].append(y - 1)
            G[y - 1].append(x - 1)
        for i in range(N):
            res[i] = ({1, 2, 3, 4} - {res[j] for j in G[i]}).pop()
        return res


if __name__ == "__main__":
    a = Solution()
    print(a.solve2(4, [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]))
