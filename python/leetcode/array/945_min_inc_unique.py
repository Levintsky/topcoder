"""
945. Minimum Increment to Make Array Unique (Medium)

Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.

Return the least number of moves to make every value in A unique. 

Example 1:

Input: [1,2,2]
Output: 1
Explanation:  After 1 move, the array could be [1, 2, 3].
Example 2:

Input: [3,2,1,2,1,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.

Note:

0 <= A.length <= 40000
0 <= A[i] < 40000
"""

class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        # tmp_max = max(A)
        result = 0
        memo = []
        for i in range(1, len(A)):
            if A[i] == A[i-1]:
                memo.append(A[i])
            elif A[i] - A[i-1] > 1 and len(memo) > 0:
                for j in range(A[i-1]+1, A[i]):
                    if len(memo) > 0:
                        item = memo.pop()
                        result += j - item
                    else:
                        break
        if len(memo) > 0:
            tmp_max = max(A)
            for item in memo:
                result += tmp_max + 1 - item
                tmp_max += 1
        return result
    
    # smarter! 
    def minIncrementForUnique(self, A):
        res = need = 0
        for i in sorted(A):
            res += max(need - i, 0)
            need = max(need + 1, i + 1)
        return res 
