"""
1223. Dice Roll Simulation (Medium)

A die simulator generates a random number from 1 to 6 for each roll. You introduced a constraint to the generator such that it cannot roll the number i more than rollMax[i] (1-indexed) consecutive times. 

Given an array of integers rollMax and an integer n, return the number of distinct sequences that can be obtained with exact n rolls.

Two sequences are considered different if at least one element differs from each other. Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:

Input: n = 2, rollMax = [1,1,2,2,2,3]
Output: 34
Explanation: There will be 2 rolls of die, if there are no constraints on the die, there are 6 * 6 = 36 possible combinations. In this case, looking at rollMax array, the numbers 1 and 2 appear at most once consecutively, therefore sequences (1,1) and (2,2) cannot occur, so the final answer is 36-2 = 34.

Example 2:

Input: n = 2, rollMax = [1,1,1,1,1,1]
Output: 30
Example 3:

Input: n = 3, rollMax = [1,1,1,2,2,3]
Output: 181

Constraints:

1 <= n <= 5000
rollMax.length == 6
1 <= rollMax[i] <= 15
"""

class Solution(object):
    def dieSimulator(self, n, rollMax):
        """
        :type n: int
        :type rollMax: List[int]
        :rtype: int
        """
        memo = {}
        MOD = 10 ** 9 + 7
        for i in range(6):
            memo[i] = [0] * rollMax[i]
            memo[i][0] = 1

        for k in range(n-1):
            new_memo = {}

            tmp_memo = {}
            for key in memo:
                tmp_memo[key] = sum(memo[key])
            total = sum(tmp_memo.values())

            for key in memo:
                new_memo[key] = [0] + memo[key][:-1]
                new_memo[key][0] = (total - tmp_memo[key]) % MOD
            memo = new_memo
        
        result = 0
        for key in memo:
            result += sum(memo[key])
        return result % MOD


if __name__ == "__main__":
    a = Solution()
    print(a.dieSimulator(2, [1,1,2,2,2,3]))
    print(a.dieSimulator(2, [1,1,1,1,1,1]))
    print(a.dieSimulator(3, [1,1,1,2,2,3]))