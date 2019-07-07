"""
1109. Corporate Flight Bookings (Medium)

There are n flights, and they are labeled from 1 to n.

We have a list of flight bookings.  The i-th booking bookings[i] = [i, j, k] means that we booked k seats from flights labeled i to j inclusive.

Return an array answer of length n, representing the number of seats booked on each flight in order of their label. 

Example 1:

Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
Output: [10,55,45,25,25]
 

Constraints:

1 <= bookings.length <= 20000
1 <= bookings[i][0] <= bookings[i][1] <= n <= 20000
1 <= bookings[i][2] <= 10000
"""

import heapq

class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        q = []
        bookings = [tuple(item) for item in bookings]
        bookings.sort()
        res = [0] * (n+1)
        ii = 0

        curr = 0
        for i in range(1, n+1):
            while ii < len(bookings) and bookings[ii][0] <= i:
                i, j, k = bookings[ii]
                heapq.heappush(q, (j, k))
                curr += k
                ii += 1
            while q and q[0][0] < i:
                j, k = heapq.heappop(q)
                curr -= k
            res[i] = curr
        return res[1:]

    def solve2(self, bookings, n):
        res = [0] * n
        for item in bookings:
            i, j, t = item
            res[i-1] += t
            if j < n:
                res[j] -= t
        for i in range(1, n):
            res[i] += res[i-1]
        return res

if __name__ == "__main__":
    a = Solution()
    print(a.corpFlightBookings([[1,2,10],[2,3,20],[2,5,25]], 5))
    print(a.solve2([[1,2,10],[2,3,20],[2,5,25]], 5))
