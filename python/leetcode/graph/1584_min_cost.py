"""
1584. Min Cost to Connect All Points (Medium)

You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

 

Example 1:



Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation:

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
Example 2:

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
Example 3:

Input: points = [[0,0],[1,1],[1,0],[-1,1]]
Output: 4
Example 4:

Input: points = [[-1000000,-1000000],[1000000,1000000]]
Output: 4000000
Example 5:

Input: points = [[0,0]]
Output: 0
 

Constraints:

1 <= points.length <= 1000
-106 <= xi, yi <= 106
All pairs (xi, yi) are distinct.
"""

class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        q = []
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                dist = sum([abs(points[i][k] - points[j][k]) for k in [0, 1]])
                heapq.heappush(q, (dist, i, j))
        
        u = [-1] * n
        edge_cnt = 0
        def find_par(idx):
            while u[idx] != -1:
                idx = u[idx]
            return idx
        
        def common_par(idx_i, idx_j):
            if idx_i == -1 and idx_j == -1:
                return min(idx_i, idx_j), True
            elif idx_i == -1:
                return idx_j, True
            elif idx_j == -1:
                return idx_i, True
            elif idx_i == idx_j:
                return idx_i, False
            else:
                return min(idx_i, idx_j), True
        
        res = 0
        
        while edge_cnt < n-1:
            d, i, j = heapq.heappop(q)
            idx_i = find_par(i)
            idx_j = find_par(j)
            
            par_idx, flag = common_par(idx_i, idx_j)
            if not flag:
                continue
            else:
                # add edge
                if idx_i != par_idx:
                    u[idx_i] = par_idx
                if idx_j != par_idx:
                    u[idx_j] = par_idx
                if i != par_idx:
                    u[i] = par_idx
                if j != par_idx:
                    u[j] = par_idx
                res += d
                edge_cnt += 1
        return res
