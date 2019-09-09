"""
1184. Distance Between Bus Stops (Easy)

A bus has n stops numbered from 0 to n - 1 that form a circle. We know the distance between all pairs of neighboring stops where distance[i] is the distance between the stops number i and (i + 1) % n.

The bus goes along both directions i.e. clockwise and counterclockwise.

Return the shortest distance between the given start and destination stops.

E.g.1
Input: distance = [1,2,3,4], start = 0, destination = 1
Output: 1
Explanation: Distance between 0 and 1 is 1 or 9, minimum is 1.

Example 2:
Input: distance = [1,2,3,4], start = 0, destination = 2
Output: 3
Explanation: Distance between 0 and 2 is 3 or 7, minimum is 3.

E.g.3
Input: distance = [1,2,3,4], start = 0, destination = 3
Output: 4
Explanation: Distance between 0 and 3 is 6 or 4, minimum is 4.
"""

class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        s, e = min(start, destination), max(start, destination)
        if s == e:
            return 0
        res_all = sum(distance)
        res1 = 0
        for i in range(s, e):
            res1 += distance[i]
        res2 = res_all - res1
        return min(res1, res2)


if __name__ == "__main__":
    a = Solution()
    print(a.distanceBetweenBusStops([1,2,3,4], 0, 1))
    print(a.distanceBetweenBusStops([1,2,3,4], 0, 2))
    print(a.distanceBetweenBusStops([1,2,3,4], 0, 3))
