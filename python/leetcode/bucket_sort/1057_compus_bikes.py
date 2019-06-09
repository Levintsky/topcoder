"""
1057. Campus Bikes (Medium)

On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M. Each worker and bike is a 2D coordinate on this grid.

Our goal is to assign a bike to each worker. Among the available bikes and workers, we choose the (worker, bike) pair with the shortest Manhattan distance between each other, and assign the bike to that worker. (If there are multiple (worker, bike) pairs with the same shortest Manhattan distance, we choose the pair with the smallest worker index; if there are multiple ways to do that, we choose the pair with the smallest bike index). We repeat this process until there are no available workers.

The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.

Return a vector ans of length N, where ans[i] is the index (0-indexed) of the bike that the i-th worker is assigned to.

Example 1:

Input: workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
Output: [1,0]
Explanation: 
Worker 1 grabs Bike 0 as they are closest (without ties), and Worker 0 is assigned Bike 1. So the output is [1, 0].
Example 2:

Input: workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]
Output: [0,2,1]
Explanation: 
Worker 0 grabs Bike 0 at first. Worker 1 and Worker 2 share the same distance to Bike 2, thus Worker 1 is assigned to Bike 2, and Worker 2 will take Bike 1. So the output is [0,2,1].

Note:

0 <= workers[i][j], bikes[i][j] < 1000
All worker and bike locations are distinct.
1 <= workers.length <= bikes.length <= 1000

"""

import heapq

class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        m = len(workers)
        n = len(bikes)
        q = []
        for i in range(m):
            for j in range(n):
                dis = sum([abs(workers[i][k]-bikes[j][k]) for k in [0, 1]])
                heapq.heappush(q, (dis, i, j))
        visited_w = set()
        visited_b = set()
        result = {}
        while len(result) < m:
            dis, i, j = heapq.heappop(q)
            if i in visited_w or j in visited_b:
                continue
            visited_w.add(i)
            visited_b.add(j)
            result[i] = j
        final_result = []
        for i in range(m):
            final_result.append(result[i])
        return final_result

    def solve2(self, workers, bikes):
        m = len(workers)
        n = len(bikes)
        dis = []
        for i in range(2000):
            dis.append([])
        for i in range(m):
            for j in range(n):
                tmp = sum([abs(workers[i][k]-bikes[j][k]) for k in [0,1]])
                dis[tmp].append((i, j))
        visited_w = set()
        visited_b = set()
        result = [-1] * m
        for d in range(2000):
            for i, j in dis[d]:
                if i in visited_w or j in visited_b:
                    continue
                visited_w.add(i)
                visited_b.add(j)
                result[i] = j
        return result


if __name__ == "__main__":
    a = Solution()
    # print(a.assignBikes([[0,0],[2,1]], [[1,2],[3,3]]))
    print(a.solve2([[0,0],[2,1]], [[1,2],[3,3]]))
    # print(a.assignBikes([[0,0],[1,1],[2,0]], [[1,0],[2,2],[2,1]]))
    print(a.solve2([[0,0],[1,1],[2,0]], [[1,0],[2,2],[2,1]]))