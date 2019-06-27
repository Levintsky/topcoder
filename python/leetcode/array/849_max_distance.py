"""
849. Maximize Distance to Closest Person (Easy)

In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.

Example 2:

Input: [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
Note:

1 <= seats.length <= 20000
seats contains only 0s or 1s, at least one 0, and at least one 1.

"""


class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        i = 0
        result = 0
        for j, item in enumerate(seats):
            if item == 1:
                i = j + 1
            else:
                if j == len(seats) - 1 or seats[j + 1] == 1:
                    # case 1: left right both have people
                    if i == 0:  # left-most
                        result = max(result, j + 1)
                    elif j == len(seats) - 1:
                        result = max(result, j - i + 1)
                    else:
                        result = max(result, (j - i) // 2 + 1)
        return result


if __name__ == "__main__":
    a = Solution()
    print(a.maxDistToClosest([1, 0, 0, 0, 1, 0, 1]))
    print(a.maxDistToClosest([1, 0, 0, 0]))
    print(a.maxDistToClosest([0, 0, 0, 1]))
    print(a.maxDistToClosest([1, 0, 0, 0, 0, 0, 1, 0, 1]))
