"""
996. Number of Squareful Arrays (Hard)

Given an array A of non-negative integers, the array is squareful if for every pair of adjacent elements, their sum is a perfect square.

Return the number of permutations of A that are squareful.  Two permutations A1 and A2 differ if and only if there is some index i such that A1[i] != A2[i].

Example 1:

Input: [1,17,8]
Output: 2
Explanation: 
[1,8,17] and [17,8,1] are the valid permutations.

Example 2:

Input: [2,2,2]
Output: 1

Note:

1 <= A.length <= 12
0 <= A[i] <= 1e9
"""

from collections import Counter
import math


class Solution(object):
    def numSquarefulPerms(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        memo = {}
        counter = dict(Counter(A))
        n = len(A)
        for i in range(n):
            for j in range(n):
                sum_ = A[i] + A[j]
                tmp = int(math.sqrt(sum_))
                if tmp ** 2 == sum_:
                    if A[i] not in memo:
                        memo[A[i]] = set([A[j]])
                    else:
                        memo[A[i]].add(A[j])
                    if A[j] not in memo:
                        memo[A[j]] = set([A[i]])
                    else:
                        memo[A[j]].add(A[i])
        self.cnt = 0

        def search(tmplist, tmpcounter):
            if len(tmplist) == n:
                self.cnt += 1
                return
            # add a new number
            k = tmplist[-1]
            if k not in memo:
                return
            for item in memo[k]:
                if tmpcounter[item] == 0:
                    continue
                tmpcounter[item] -= 1
                tmplist.append(item)
                search(tmplist, tmpcounter)
                _ = tmplist.pop()
                tmpcounter[item] += 1

        A.sort()
        for i, item in enumerate(A):
            if i > 0 and item == A[i - 1]:
                continue
            list_ = [item]
            counter[item] -= 1
            search(list_, counter)
            counter[item] += 1
        return self.cnt


if __name__ == "__main__":
    a = Solution()
    print(a.numSquarefulPerms([1, 17, 8]))
    print(a.numSquarefulPerms([2, 2, 2]))
    print(a.numSquarefulPerms([1, 1]))
