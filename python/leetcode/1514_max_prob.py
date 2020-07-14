import heapq


class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start: int
        :type end: int
        :rtype: float
        """
        memo = {} # node to dict
        for i in range(n):
            memo[i] = {}
        for edge, prob in zip(edges, succProb):
            i, j = edge
            memo[i][j] = prob
            memo[j][i] = prob
        
        q = [(-1., start)]
        res = {}
        while len(q) > 0 and end not in res:
            p, ind = heapq.heappop(q)
            if ind in res:
                continue
            else:
                p = -p
                res[ind] = p
            for i in memo[ind]:
                if i in res:
                    continue
                newprob = p * memo[ind][i]
                if i not in res:
                    heapq.heappush(q, (-newprob, i))
        if end in res:
            return res[end]
        else:
            return 0.
            

if __name__ == "__main__":
    a = Solution()
    print(a.maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2))
    print(a.maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.3], 0, 2))
    print(a.maxProbability(3, [[0,1]], [0.5], 0, 2))
    print(a.maxProbability(500, [[193,229],[133,212],[224,465]], [0.91,0.78,0.64], 4, 364))
