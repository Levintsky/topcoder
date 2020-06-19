"""
1473. Paint House III (Hard)

There is a row of m houses in a small city, each house must be painted with one of the n colors (labeled from 1 to n), some houses that has been painted last summer should not be painted again.

A neighborhood is a maximal group of continuous houses that are painted with the same color. (For example: houses = [1,2,2,3,3,2,1,1] contains 5 neighborhoods  [{1}, {2,2}, {3,3}, {2}, {1,1}]).

Given an array houses, an m * n matrix cost and an integer target where:

houses[i]: is the color of the house i, 0 if the house is not painted yet.
cost[i][j]: is the cost of paint the house i with the color j+1.
Return the minimum cost of painting all the remaining houses in such a way that there are exactly target neighborhoods, if not possible return -1.

 

Example 1:

Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
Output: 9
Explanation: Paint houses of this way [1,2,2,1,1]
This array contains target = 3 neighborhoods, [{1}, {2,2}, {1,1}].
Cost of paint all houses (1 + 1 + 1 + 1 + 5) = 9.
Example 2:

Input: houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
Output: 11
Explanation: Some houses are already painted, Paint the houses of this way [2,2,1,2,2]
This array contains target = 3 neighborhoods, [{2,2}, {1}, {2,2}]. 
Cost of paint the first and last house (10 + 1) = 11.
Example 3:

Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[1,10],[10,1],[1,10]], m = 5, n = 2, target = 5
Output: 5
Example 4:

Input: houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3
Output: -1
Explanation: Houses are already painted with a total of 4 neighborhoods [{3},{1},{2},{3}] different of target = 3.
 

Constraints:

m == houses.length == cost.length
n == cost[i].length
1 <= m <= 100
1 <= n <= 20
1 <= target <= m
0 <= houses[i] <= n
1 <= cost[i][j] <= 10^4
"""

class Solution(object):
    def minCost(self, houses, cost, m, n, target):
        """
        :type houses: List[int]
        :type cost: List[List[int]]
        :type m: int
        :type n: int
        :type target: int
        :rtype: int
        """
        # wrong dfs will be TLE
        todos = [i for i in range(m) if houses[i] == 0]

        # sort cost
        sort_cost = []
        for i, tmpcost in enumerate(cost):
            newcost = zip(tmpcost, range(1,n+1))
            newcost.sort()
            newcost = [(item[1], item[0]) for item in newcost]
            sort_cost.append(newcost)
        # print(cost)
        # print(sort_cost)
        # return

        # sanity check
        def check_cnt():
            diffs = []
            for item in houses:
                if item == 0:
                    continue
                if len(diffs) == 0 or item != diffs[-1]:
                    diffs.append(item)
            return len(diffs)

        # houses = [1,2,1,0,0]
        # print(check_cnt())
        # exit()

        if check_cnt() > target:
            return -1
        if len(todos) == 0:
            if check_cnt() == target:
                return 0
            else:
                return -1

        def calculate_cost():
            tmpres = 0
            for i, item in enumerate(houses):
                if item > 0:
                    tmpres += cost[i][item-1]
            return tmpres

        self.result = float('inf')

        def dfs(idx):
            print('work on', idx)
            # work on todos[idx]
            r_idx = todos[idx]
            if idx == len(todos) - 1: # edge case
                for c, _ in sort_cost[r_idx]: # range(1, n+1):
                    houses[r_idx] = c
                    if check_cnt() == target:
                        # calculate cost
                        tmpres = calculate_cost()
                        self.result = min(tmpres, self.result)
                houses[r_idx] = 0
            else:
                # for i in range(1, n+1):
                for c, _ in sort_cost[r_idx]:
                    houses[r_idx] = c
                    tmp_cnt = check_cnt()
                    if tmp_cnt > target: # too many colors
                        continue
                    if tmp_cnt + len(todos) -1 - idx < target: # too few
                        continue
                    if calculate_cost() > self.result:
                        continue
                    dfs(idx+1)
                houses[r_idx] = 0

        dfs(0)
        if self.result == float('inf'):
            return -1
        result = self.result - calculate_cost()
        return result

    def solve2(self, houses, cost, m, n, target):

        memo = {}
        if houses[-1] == 0:
            for i, c in enumerate(cost[-1]):
                memo[1, i+1] = c
        else:
            memo[1, houses[-1]] = 0
        # print(memo)

        for ind in range(m-2, -1, -1):
            new_memo = {}
            # case 1: occupied
            if houses[ind] > 0:
                for k, color in memo.keys():
                    if color == houses[ind]:
                        new_memo[k, houses[ind]] = min(new_memo.get((k, houses[ind]), float('inf')), memo[k, color])
                    else:
                        new_memo[k+1, houses[ind]] = min(new_memo.get((k+1, houses[ind]),float('inf')), memo[k, color])
            else: # not occupied
                for c in range(1, n+1):
                    for k, color in memo.keys():
                        if c == color:
                            new_memo[k, c] = min(new_memo.get((k,c), float('inf')), memo[k, color] + cost[ind][c-1])
                        else:
                            new_memo[k+1, c] = min(new_memo.get((k+1,c), float('inf')), memo[k, color] + cost[ind][c-1])
            memo = new_memo
            keys = memo.keys()
            for k in keys:
                if k[0] > target:
                    del memo[k]
    
        result = float('inf')
        for k in memo.keys():
            if k[0] == target:
                result = min(result, memo[k])
        if result == float('inf'):
            return -1
        return result

    def solve3(self, A, cost, m, n, target):
        dp, dp2 = {(0, 0): 0}, {}
        for i, a in enumerate(A):
            for cj in (range(1, n + 1) if a == 0 else [a]):
                for ci, b in dp:
                    b2 = b + (ci != cj)
                    if b2 > target: continue
                    dp2[cj, b2] = min(dp2.get((cj,b2), float('inf')), dp[ci, b] + (cost[i][cj - 1] if cj != a else 0))
            dp, dp2 = dp2, {}
        return min([dp[c, b] for c, b in dp if b == target] or [-1])


if __name__ == "__main__":
    a = Solution()
    """
    print(a.solve2([0,0,0,0,0], [[1,10],[10,1],[10,1],[1,10],[5,1]], 5, 2, 3))
    print(a.solve2([0,2,1,2,0], [[1,10],[10,1],[10,1],[1,10],[5,1]], 5, 2, 3))
    print(a.solve2([0,0,0,0,0], [[1,10],[10,1],[1,10],[10,1],[1,10]], 5, 2, 5))
    print(a.solve2([3,1,2,3], [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], 4, 3, 3))
    print(a.solve2([2,2,1], [[1,1],[3,4],[4,2]], 3, 2, 2))
    print(a.solve2([1,1,1,0,2,0,0,2,0,0], [[6,8,5],[4,8,3],[7,1,10],[4,9,8],[4,7,6],[6,5,1],[8,9,4],[7,6,3],[9,5,10],[8,8,4]], 10, 3, 10))
    """
    houses = [4,0,0,0,4,11,0,0,0,0,3,0,0,0,0,5,0,0,0,0,0,8,2,2,0]
    cost = [[33,13,38,3,25,10,49,9,10,36,39,3],[47,19,6,37,2,23,50,18,46,14,24,33],[32,31,32,17,36,41,43,29,36,29,47,3],[25,27,5,31,1,17,27,46,10,8,31,49],[50,16,33,24,42,2,33,39,43,31,2,38],[38,6,23,18,9,13,31,36,28,7,7,1],[40,23,21,5,48,2,18,24,6,27,39,44],[25,43,4,9,5,5,30,42,23,41,7,15],[45,32,44,15,5,1,2,43,49,30,29,4],[39,26,42,45,27,28,41,6,42,27,4,43],[32,2,43,13,15,30,32,12,36,5,19,22],[12,23,13,8,8,9,32,43,46,41,43,8],[10,18,27,2,7,40,44,50,32,29,42,10],[50,7,15,9,32,9,15,10,15,41,10,36],[48,6,26,6,14,37,44,47,4,44,1,30],[34,46,12,32,19,1,18,31,1,16,44,48],[15,35,17,14,16,29,23,18,28,26,45,17],[43,45,7,39,37,18,18,33,24,47,27,46],[17,12,15,20,44,34,14,8,28,40,12,21],[18,10,15,47,21,7,47,34,37,49,16,24],[19,3,38,14,32,21,4,25,34,3,33,23],[21,45,3,49,45,40,38,10,30,5,37,21],[29,38,43,22,44,26,3,18,45,40,40,17],[21,12,30,23,4,25,32,43,37,15,35,30],[38,14,6,21,3,43,43,30,9,19,39,17]]
    m = 25
    n = 12
    target = 15
    print(a.solve3(houses, cost, m, n, target))
