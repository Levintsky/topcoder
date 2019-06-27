"""
1029. Two City Scheduling (Easy)

There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

Example 1:

Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
"""


class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        pure1 = []

        for a, b in costs:
            pure1.append(a - b)
        pure1.sort()
        N = len(pure1)
        pure1 = pure1[: N // 2]
        res1 = sum(pure1)
        res2 = sum([item[1] for item in costs])
        return res1 + res2


if __name__ == "__main__":
    a = Solution()
    print(a.twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]]))
