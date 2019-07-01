"""
1103. Distribute Candies to People (Easy)

We distribute some number of candies, to a row of n = num_people people in the following way:

We then give 1 candy to the first person, 2 candies to the second person, and so on until we give n candies to the last person.

Then, we go back to the start of the row, giving n + 1 candies to the first person, n + 2 candies to the second person, and so on until we give 2 * n candies to the last person.

This process repeats (with us giving one more candy each time, and moving to the start of the row after we reach the end) until we run out of candies.  The last person will receive all of our remaining candies (not necessarily one more than the previous gift).

Return an array (of length num_people and sum candies) that represents the final distribution of candies. 

Example 1:

Input: candies = 7, num_people = 4
Output: [1,2,3,1]
Explanation:
On the first turn, ans[0] += 1, and the array is [1,0,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0,0].
On the third turn, ans[2] += 3, and the array is [1,2,3,0].
On the fourth turn, ans[3] += 1 (because there is only one candy left), and the final array is [1,2,3,1].
Example 2:

Input: candies = 10, num_people = 3
Output: [5,2,3]
Explanation: 
On the first turn, ans[0] += 1, and the array is [1,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0].
On the third turn, ans[2] += 3, and the array is [1,2,3].
On the fourth turn, ans[0] += 4, and the final array is [5,2,3].

Constraints:

1 <= candies <= 10^9
1 <= num_people <= 1000
"""

import math


class Solution(object):
    def minHeightShelves(self, books, shelf_width):
        """
        :type books: List[List[int]]
        :type shelf_width: int
        :rtype: int
        """
        curr = [0, 0, 0] # all, w, h
        for b in books[::-1]:
            if b[0] + curr[1] <= shelf_width:
                curr[1] += b[0]
                curr[2] = max(curr[2], b[1])
            else:
            	curr = [curr[0]+curr[2], b[0], b[1]]
            print(curr)
        return curr[0] + curr[2]

    def solve2(self, books, shelf_width):
        # logically correct, will TLE
        def dfs(i, base, curr):
            # curr: [w, h]
            # edge case 1:
            if i == len(books) - 1:
                if books[i][0] + curr[0] <= shelf_width:
                    # curr = [curr[0]+books[i][0], max(curr[1], books[i][1])]
                    return max(curr[1], books[i][1]) + base
                else:
                    return base + curr[1] + books[i][1]
            if curr[0] == 0 and curr[1] == 0:
                curr = [books[i][0], books[i][1]]
                return dfs(i+1, base, curr)
            if books[i][1] <= curr[1] or books[i][0] + curr[0] > shelf_width:
                if books[i][0] + curr[0] <= shelf_width:
                    curr = [curr[0]+books[i][0], max(curr[1], books[i][1])]
                    return dfs(i+1, base, curr)
                else:
                    base += curr[1]
                    curr = [books[i][0], books[i][1]]
                    return dfs(i+1, base, curr)
            else:
                # option 1: put in the same line
                new_curr = [curr[0]+books[i][0], max(curr[1], books[i][1])]
                res1 = dfs(i+1, base, new_curr)
                # option 2: put in a new line
                base += curr[1]
                curr = [books[i][0], books[i][1]]
                res2 = dfs(i+1, base, curr)
                return min(res1, res2)
        res = dfs(0, 0, [0, 0])
        return res

    def solve3(self, books, shelf_width):
        def place(st):
            if st == len(books):
                return 0
            if st in cache:
                return cache[st]
            width, res, maxh = 0, math.inf, 0
            for i in range(st, len(books)):
                if width + books[i][0] <= shelf_width:
                    width += books[i][0] 
                    maxh = max(maxh, books[i][1])
                    res = min(res, maxh+place(i+1))
                else:
                    break
            cache[st] = res
            return cache[st]
        cache = {}
        res = place(0)
        return res

    def solve4(self, books, shelf_width):
        # dp[i]: the min height with a shelve ends with books i-1
        dp = [0] * (len(books) + 1)
        for i in range(1, len(books)+1):
            width = books[i-1][0]
            height = books[i-1][1]
            dp[i] = dp[i-1] + height
            j = i - 1
            while j > 0 and width + books[j-1][0] <= shelf_width:
                height = max(height, books[j-1][1])
                width += books[j-1][0]
                dp[i] = min(dp[i], dp[j-1]+height)
                j -= 1
        return dp[-1]

if __name__ == "__main__":
    a = Solution()
    # print(a.minHeightShelves([[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], 4))
    # print(a.minHeightShelves([[2,2],[2,2],[1,1],[1,1]], 4))
    # print(a.solve2([[1,1],[2,3],[2,3]], 4))
    # print(a.solve3([[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], 4))
    print(a.solve4([[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], 4))