"""
1004. Max Consecutive Ones III (Medium)

Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s. 

Example 1:

Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation: 
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
Example 2:

Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation: 
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

Note:

1 <= A.length <= 20000
0 <= K <= A.length
A[i] is 0 or 1 
"""

"""
typical sliding window problem of array:
A[i]..A[j] keeps best solution

solution 2: optimization
don't need to update i, since we want to get max
"""


class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        i = 0  # start
        result = 0
        for j in range(len(A)):
            if A[j] == 0:
                K -= 1
                if K == -1:
                    while K < 0:
                        if A[i] == 0:
                            # i += 1
                            K += 1
                            # break
                        i += 1
            result = max(result, j - i + 1)
        return result

    def longestOnes2(self, A, K):
        i = 0  # start
        result = 0
        for j in range(len(A)):
            if A[j] == 0:
                K -= 1
            if K < 0:
                K += 1 - A[i]
                i += 1
            result = max(result, j - i + 1)
        return result


if __name__ == "__main__":
    a = Solution()
    print(a.longestOnes2([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
    print(a.longestOnes2([0, 1, 0, 0, 1, 1, 0], 0))
