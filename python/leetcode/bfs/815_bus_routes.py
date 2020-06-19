"""
815. Bus Routes (Hard)

We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever. For example if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever.

We start at bus stop S (initially not on a bus), and we want to go to bus stop T. Travelling by buses only, what is the least number of buses we must take to reach our destination? Return -1 if it is not possible.

Example:
Input: 
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
Output: 2
Explanation: 
The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
 

Constraints:

1 <= routes.length <= 500.
1 <= routes[i].length <= 10^5.
0 <= routes[i][j] < 10 ^ 6.
"""

import collections


class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T:
            return 0
        
        s_set, t_set = set(), set()
        for i, l in enumerate(routes):
            routes[i] = set(routes[i])
            if S in routes[i]:
                s_set.add(i)
            if T in routes[i]:
                t_set.add(i)
                
        # bus connectivity
        memo = {}
        n = len(routes)
        for i in range(n):
            for j in range(i+1, n):
                if len(routes[i].intersection(routes[j])) > 0:
                    if i not in memo:
                        memo[i] = []
                    memo[i].append(j)
                    if j not in memo:
                        memo[j] = []
                    memo[j].append(i)
        
        # bfs until anything in t_set is visited
        step = 1
        visited = set()
        q = collections.deque([item for item in s_set]) # bus set
        while len(q) > 0:
            new = set()
            
            while len(q) > 0:
                item = q.popleft()
                visited.add(item)
                if item in t_set:
                    return step
                
                if item not in memo:
                    continue
                for nei in memo[item]:
                    if nei not in visited:
                        new.add(nei)
            for item in new:
                q.append(item)
            step += 1
        return -1
            
            


if __name__ == "__main__":
    a = Solution()
    print(a.numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6))
    print(a.numBusesToDestination([[7,12],[4,5,15],[6],[15,19],[9,12,13]], 15, 12))
    print(a.numBusesToDestination([[1],[15,16,18],[10],[3,4,12,14]], 3, 15))