"""
1515. Best Position for a Service Centre (Hard)

A delivery company wants to build a new service centre in a new city. The company knows the positions of all the customers in this city on a 2D-Map and wants to build the new centre in a position such that the sum of the euclidean distances to all customers is minimum.

Given an array positions where positions[i] = [xi, yi] is the position of the ith customer on the map, return the minimum sum of the euclidean distances to all customers.

In other words, you need to choose the position of the service centre [xcentre, ycentre] such that the following formula is minimized:


Answers within 10^-5 of the actual value will be accepted.

 

Example 1:


Input: positions = [[0,1],[1,0],[1,2],[2,1]]
Output: 4.00000
Explanation: As shown, you can see that choosing [xcentre, ycentre] = [1, 1] will make the distance to each customer = 1, the sum of all distances is 4 which is the minimum possible we can achieve.
Example 2:


Input: positions = [[1,1],[3,3]]
Output: 2.82843
Explanation: The minimum possible sum of distances = sqrt(2) + sqrt(2) = 2.82843
Example 3:

Input: positions = [[1,1]]
Output: 0.00000
Example 4:

Input: positions = [[1,1],[0,0],[2,0]]
Output: 2.73205
Explanation: At the first glance, you may think that locating the centre at [1, 0] will achieve the minimum sum, but locating it at [1, 0] will make the sum of distances = 3.
Try to locate the centre at [1.0, 0.5773502711] you will see that the sum of distances is 2.73205.
Be careful with the precision!
Example 5:

Input: positions = [[0,1],[3,2],[4,5],[7,6],[8,9],[11,1],[2,12]]
Output: 32.94036
Explanation: You can use [4.3460852395, 4.9813795505] as the position of the centre.
 

Constraints:

1 <= positions.length <= 50
positions[i].length == 2
0 <= positions[i][0], positions[i][1] <= 100
"""

import math


class Solution(object):
    def getMinDistSum(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: float
        """
        n = len(positions)
        if n == 1:
            return 0.
        curr = [0., 0.]
        for x, y in positions:
            curr[0] += x
            curr[1] += y
        curr = [item / n for item in curr]

        def get_diff(positions, curr):
            diff = [[pos[0]-curr[0], pos[1]-curr[1]] for pos in positions]
            return diff

        def get_dist(diff, eps=1.e-10):
            dist = [d[0] ** 2 + d[1] ** 2 for d in diff]
            dist = [math.sqrt(item) + eps for item in dist]
            return dist

        def get_grad(diff, dist):
            grad = [[dif[0]/dis, dif[1]/dis] for dif, dis in zip(diff, dist)]
            grad = [sum([item[0] for item in grad]) / n, sum([item[1] for item in grad]) / n]
            return grad

        last_dist = 1000000.
        # iter_ = 1.
        while True:
        # for i in range(100):
            # get diff
            diff = get_diff(positions, curr)

            # get dist
            dist = get_dist(diff)

            # get grad
            grad = get_grad(diff, dist)

            curr = [curr[0] + grad[0]/2., curr[1] + grad[1]/2.]
            # iter_ += 1.

            real_dist = get_dist(diff, 0.)
            dist_sum = sum(real_dist)
            print(curr, dist_sum)

            if last_dist - dist_sum < 1.e-8:
                break
            else:
                last_dist = dist_sum

        # dist = get_dist(diff, 0.)
        return dist_sum


if __name__ == "__main__":
    a = Solution()
    """
    print(a.getMinDistSum([[0,1],[1,0],[1,2],[2,1]]))
    print(a.getMinDistSum([[1,1],[3,3]]))
    print(a.getMinDistSum([[1,1]]))
    print(a.getMinDistSum([[1,1], [1,1]]))
    print(a.getMinDistSum([[1,1],[0,0],[2,0]]))
    print(a.getMinDistSum([[0,1],[3,2],[4,5],[7,6],[8,9],[11,1],[2,12]]))
    print(a.getMinDistSum([[9,9],[31,1],[28,61],[14,42],[95,98],[37,69]]))
    """
    print(a.getMinDistSum([[44,23],[18,45],[6,73],[0,76],[10,50],[30,7],[92,59],[44,59],[79,45],[69,37],[66,63],[10,78],[88,80],[44,87]]))
