"""
977. Squares of a Sorted Array (Easy)

Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

 

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.
"""

"""
Keypoints: two pointers
can go from middle -> left, right
or left, right -> middle
"""

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # step 1: find idx >= 0
        idx = 0
        while idx < len(A) and A[idx] < 0:
        	idx += 1
        result = []
        i, j = idx - 1, idx
        while i >= 0 or j < len(A):
        	if j == len(A) or (i >= 0 and A[i] ** 2 <= A[j] ** 2):
        		result.append(A[i] ** 2)
        		i -= 1
        	else:
        		result.append(A[j] ** 2)
        		j += 1
        return result

    def solve2(self, A):
    	answer = collections.deque()
		l, r = 0, len(A) - 1
		while l <= r:
			left, right = abs(A[l]), abs(A[r])
			if left > right:
				answer.appendleft(left * left)
				l += 1
			else:
				answer.appendleft(right * right)
				r -= 1
		return list(answer)

	def solve3(self, A):
		answer = [0] * len(A)
		l, r = 0, len(A) - 1
		while l <= r:
			left, right = abs(A[l]), abs(A[r])
			if left > right:
				answer[r - l] = left * left
				l += 1
			else:
				answer[r - l] = right * right
				r -= 1
		return answer

if __name__ == "__main__":
	a = Solution()
	print(a.sortedSquares([-4,-1,0,3,10]))
	print(a.sortedSquares([-7,-3,2,3,11]))

