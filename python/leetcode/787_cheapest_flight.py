"""
787. Cheapest Flights Within K Stops (Medium)

There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation: 
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
Example 2:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation: 
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
Note:

The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be (src, dst, price).
The price of each flight will be in the range [1, 10000].
k is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles.
"""

import heapq
import collections


class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        self.memo = {}
        for i in range(n):
            self.memo[i] = []

        for f in flights:
            s, t, time = f
            heapq.heappush(self.memo[s], (time, t))

        last = [src]
        # result = {src: [(0,0)]} # (t, stop)
        result = {src: 0}
        for i in range(K + 1):
            # i stops
            curr = []
            while len(last) != 0:
                tmps = last.pop()
                while len(self.memo[tmps]) > 0:
                    tmpt, tmpd = heapq.heappop(self.memo[tmps])
                    if tmpd not in result:
                        result[tmpd] = tmpt + result[tmpd]  # [(tmpt+)]
                        curr.append(src)
                    # elif tmpt + result[tmps][0][0] < result[tmpd][0][0]:
                    elif tmpt + result[tmps] < result[tmpd]:
                        return

    def solve2(self, n, flights, src, dst, k):
        f = collections.defaultdict(dict)
        for a, b, p in flights:
            f[a][b] = p
        heap = [(0, src, k + 1)]
        while heap:
            p, i, k = heapq.heappop(heap)
            if i == dst:
                return p
            if k > 0:
                for j in f[i]:
                    heapq.heappush(heap, (p + f[i][j], j, k - 1))
        return -1


if __name__ == "__main__":
    a = Solution()
    print(a.solve2(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1))
