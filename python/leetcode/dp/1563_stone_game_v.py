"""
1563. Stone Game V (Hard)

There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.

In each round of the game, Alice divides the row into two non-empty rows (i.e. left row and right row), then Bob calculates the value of each row which is the sum of the values of all the stones in this row. Bob throws away the row which has the maximum value, and Alice's score increases by the value of the remaining row. If the value of the two rows are equal, Bob lets Alice decide which row will be thrown away. The next round starts with the remaining row.

The game ends when there is only one stone remaining. Alice's is initially zero.

Return the maximum score that Alice can obtain.

 

Example 1:

Input: stoneValue = [6,2,3,4,5,5]
Output: 18
Explanation: In the first round, Alice divides the row to [6,2,3], [4,5,5]. The left row has the value 11 and the right row has value 14. Bob throws away the right row and Alice's score is now 11.
In the second round Alice divides the row to [6], [2,3]. This time Bob throws away the left row and Alice's score becomes 16 (11 + 5).
The last round Alice has only one choice to divide the row which is [2], [3]. Bob throws away the right row and Alice's score is now 18 (16 + 2). The game ends because only one stone is remaining in the row.
Example 2:

Input: stoneValue = [7,7,7,7,7,7,7]
Output: 28
Example 3:

Input: stoneValue = [4]
Output: 0
 

Constraints:

1 <= stoneValue.length <= 500
1 <= stoneValue[i] <= 10^6
"""

import pdb

class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        self.cum = [0]
        for item in stoneValue:
            self.cum.append(self.cum[-1] + item)
            
        memo = {} # (i, j)
        # pdb.set_trace()
        def dp(i, j):
            if (i, j) in memo:
                return memo[i, j]
            if i >= j:
                return 0
            if i + 1 == j:
                memo[i, j] = min(stoneValue[i], stoneValue[j])
                return memo[i, j]
            best = 0
            for k in range(i, j):
                # l: [i..k], r: [k+1..j]
                sum_l = self.cum[k+1] - self.cum[i]
                sum_r = self.cum[j+1] - self.cum[k+1]
                if sum_l > sum_r:
                    tmp = sum_r + dp(k+1, j)
                elif sum_l < sum_r:
                    tmp = sum_l + dp(i, k)
                else:
                    tmp = sum_l + max(dp(i, k), dp(k+1, j))
                best = max(best, tmp)
            memo[i, j] = best
            return best
        res = dp(0, len(stoneValue)-1)
        print(memo) 
        return res


if __name__ == "__main__":
    a = Solution()
    print(a.stoneGameV([6,2,3,4,5,5]))
    print(a.stoneGameV([7,7,7,7,7,7,7]))
    print(a.stoneGameV([4]))
    print(a.stoneGameV([1,1,2]))
    # print(a.stoneGameV([6,2,3]))
