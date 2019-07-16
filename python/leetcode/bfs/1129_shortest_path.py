"""
1129. Shortest Path with Alternating Colors (Medium)

Consider a directed graph, with nodes labelled 0, 1, ..., n-1.  In this graph, each edge is either red or blue, and there could be self-edges or parallel edges.

Each [i, j] in red_edges denotes a red directed edge from node i to node j.  Similarly, each [i, j] in blue_edges denotes a blue directed edge from node i to node j.

Return an array answer of length n, where each answer[X] is the length of the shortest path from node 0 to node X such that the edge colors alternate along the path (or -1 if such a path doesn't exist).

Example 1:

Input: n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
Output: [0,1,-1]
Example 2:

Input: n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
Output: [0,1,-1]
Example 3:

Input: n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
Output: [0,-1,-1]
Example 4:

Input: n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
Output: [0,1,2]
Example 5:

Input: n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
Output: [0,1,1]
 

Constraints:

1 <= n <= 100
red_edges.length <= 400
blue_edges.length <= 400
red_edges[i].length == blue_edges[i].length == 2
0 <= red_edges[i][j], blue_edges[i][j] < n
"""


import collections


class Solution(object):
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        """
        :type n: int
        :type red_edges: List[List[int]]
        :type blue_edges: List[List[int]]
        :rtype: List[int]
        """
        def edges2memo(edges):
            memo = {}
            for src, tgt in edges:
                if src not in memo:
                    memo[src] = []
                memo[src].append(tgt)
            return memo

        self.memo_red = edges2memo(red_edges)
        self.memo_blue = edges2memo(blue_edges)

        self.result = [float('inf')] * n
        self.result[0] = 0

        # bfs
        self.bfs('r', 'b')
        self.bfs('b', 'r')
        for i in range(n):
        	if not self.result[i] < float('inf'):
        	    self.result[i] = -1
        return self.result

    def bfs(self, next_, now):
        visited_r = set()
        visited_b = set()
        q = collections.deque()
        q.append(0)
        cnt = 0
        while q:
            q2 = collections.deque()
            if next_ == 'r':
                tmp_memo = self.memo_red
                visit_now, visit_next = visited_b, visited_r
            else:
                tmp_memo = self.memo_blue
                visit_now, visit_next = visited_r, visited_b
            while q:
                n = q.pop()
                if n not in visit_now:
                    visit_now.add(n)
                    self.result[n] = min(self.result[n], cnt)
                    if n in tmp_memo:
                        for e in tmp_memo[n]:
                            if e not in visit_next:
                                q2.append(e)
            next_, now = now, next_
            q = q2
            cnt += 1

    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        G = [[[], []] for i in xrange(n)]
        for i, j in red_edges: G[i][0].append(j)
        for i, j in blue_edges: G[i][1].append(j)
        res = [[0, 0]] + [[n * 2, n * 2] for i in xrange(n - 1)]
        bfs = [[0, 0], [0, 1]]
        for i, c in bfs:
            for j in G[i][c]:
                if res[j][c] == n * 2:
                    res[j][c] = res[i][1 - c] + 1
                    bfs.append([j, 1 - c])
        return [x if x < n * 2 else -1 for x in map(min, res)]

if __name__ == "__main__":
    a = Solution()
    print(a.shortestAlternatingPaths(3, [[0,1],[1,2]], [[1,1]]))
    print(a.shortestAlternatingPaths(3, [[1,1]], [[0,1],[1,2]]))
    print(a.shortestAlternatingPaths(3, [[0,1]], [[2,1]]))
    print(a.shortestAlternatingPaths(3, [[0,1]], [[1,2]]))
    print(a.shortestAlternatingPaths(3, [[0,1],[0,2]], [[1,0]]))
