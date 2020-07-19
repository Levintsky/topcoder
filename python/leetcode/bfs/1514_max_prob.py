"""
1514. Path with Maximum Probability (Medium)

You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

 

Example 1:

Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.
Example 2:



Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
Output: 0.30000
Example 3:



Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
Output: 0.00000
Explanation: There is no path between 0 and 2.
 

Constraints:

2 <= n <= 10^4
0 <= start, end < n
start != end
0 <= a, b < n
a != b
0 <= succProb.length == edges.length <= 2*10^4
0 <= succProb[i] <= 1
There is at most one edge between every two nodes.
"""


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
