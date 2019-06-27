"""
992. Subarrays with K Different Integers (Hard)

Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the number of different integers in that subarray is exactly K.

(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

Return the number of good subarrays of A.

 

Example 1:

Input: A = [1,2,1,2,3], K = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
Example 2:

Input: A = [1,2,1,3,4], K = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
 

Note:

1 <= A.length <= 20000
1 <= A[i] <= A.length
1 <= K <= A.length
"""

"""
Solution 1: O(KN), will TLE
A[i..j]: K+1

for an item key, record:
  (1) how many times cnt;
  (2) where a number last appears;
if memo[k]=(cnt, t), remove all numbers before index t will still maintain the number
time complexity: O(N) numbers x O(K) for min() operator every time
"""

"""
Solution 2:

Write a helper using sliding window,
to get the number of subarrays with at most K distinct elements.
Then f(exactly K) = f(atMost K) - f(atMost K-1).

Of course, you can merge 2 for loop into ones, if you like.

Time Complexity:
O(N)
"""

import collections


class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        return self.atMostK(A, K) - self.atMostK(A, K - 1)

    def atMostK(self, A, K):
        count = collections.Counter()
        res = i = 0
        for j in range(len(A)):
            if count[A[j]] == 0:
                K -= 1
            count[A[j]] += 1
            while K < 0:
                count[A[i]] -= 1
                if count[A[i]] == 0:
                    K += 1
                i += 1
            res += j - i + 1
        return res

    def solve2(self, A, K):
        memo = {}
        result = 0
        begin = 0
        for j in range(len(A)):
            memo[A[j]] = j
            if len(memo) == K + 1:
                min_index = min(memo.values())
                begin = min_index + 1
                del memo[A[min_index]]
            if len(memo) == K:  # case
                # find minimum in values()
                min_index = min(memo.values())
                result += min_index - begin + 1
        return result


if __name__ == "__main__":
    a = Solution()
    print(a.subarraysWithKDistinct([1, 2, 1, 2, 3], 2))
    print(a.solve2([1, 2, 1, 2, 3], 2))
