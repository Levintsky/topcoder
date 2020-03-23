"""
1386. Cinema Seat Allocation (Medium)

A cinema has n rows of seats, numbered from 1 to n and there are ten seats in each row, labelled from 1 to 10 as shown in the figure above.

Given the array reservedSeats containing the numbers of seats already reserved, for example, reservedSeats[i]=[3,8] means the seat located in row 3 and labelled with 8 is already reserved. 

Return the maximum number of four-person families you can allocate on the cinema seats. A four-person family occupies fours seats in one row, that are next to each other. Seats across an aisle (such as [3,3] and [3,4]) are not considered to be next to each other, however, It is permissible for the four-person family to be separated by an aisle, but in that case, exactly two people have to sit on each side of the aisle.

Input: n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
Output: 4
Explanation: The figure above shows the optimal allocation for four families, where seats mark with blue are already reserved and contiguous seats mark with orange are for one family. 
Example 2:

Input: n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
Output: 2
Example 3:

Input: n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
Output: 4

Constraints:

1 <= n <= 10^9
1 <= reservedSeats.length <= min(10*n, 10^4)
reservedSeats[i].length == 2
1 <= reservedSeats[i][0] <= n
1 <= reservedSeats[i][1] <= 10
All reservedSeats[i] are distinct.
"""

class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        # logically correct, but will be out of memory
        memo = {}
        for i in range(1, n+1):
            memo[i] = []
        for i, j in reservedSeats:
            memo[i].append(j)
        # print(memo)
        set_ = set([0,2,4,6])

        cnt = 0
        for i in range(1, n+1):
            # if len(memo[i]) == 0:
            #   cnt += 2
            memo[i].sort()
            memo[i].insert(0, 0)
            memo[i].append(11)
            for j in range(len(memo[i])-1):
                if memo[i][j+1] - memo[i][j] > 4:
                    if memo[i][j+1] - memo[i][j] == 5:
                        if memo[i][j] in set_:
                            continue
                    if memo[i][j] <= 1 and memo[i][j+1] >= 10:
                        cnt += 2
                    else:
                        cnt += 1
            # print(i, cnt)
        return cnt

    def solve2(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = collections.defaultdict(int) 
        res = 0
        
        for row, col in reservedSeats:
            seats[row] = seats[row] | (1 << (col-1))

        for reserved in seats.values():
            curr = 0
            curr += (reserved & int('0111100000', 2)) == 0
            curr += (reserved & int('0000011110', 2)) == 0
            curr += (reserved & int('0001111000', 2)) == 0 and curr == 0

            res += curr    

        return res + 2 * (n - len(seats))


if __name__ == "__main__":
    a = Solution()
    print(a.maxNumberOfFamilies(3, [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]))
    print(a.maxNumberOfFamilies(2, [[2,1],[1,8],[2,6]]))
    print(a.maxNumberOfFamilies(4, [[4,3],[1,4],[4,6],[1,7]]))
    print(a.maxNumberOfFamilies(4, [[2,10],[3,1],[1,2],[2,2],[3,5],[4,1],[4,9],[2,7]]))
