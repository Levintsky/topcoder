# Array

## Subarray Sum
- Find sum:
	- LC-523: Continuous Subarray Sum: continuous subarray of size at least 2 that sums up to a multiple of k, return true/false
		- 1-D integral image
	- **LC-363**: Max Sum of Rectangle No Larger Than K
	- LC-1074: Number of Submatrices That Sum to Target
- Find array:
	- **LC-862**: Shortest Subarray with Sum at Least K
- Kadane's Algorithm to Maximum Sum Subarray Problem
	- https://www.youtube.com/watch?v=86CQq3pKSUw
	- 1-D case: O(n), brute-force O(n^2)
	```python
	def kadane(A):
	    max_cur = max_global = A[0]
	    for i in range(1, len(A)-1):
	        max_cur = max(A[i], A[i]+max_cur)
	        max_global = max(max_global, max_cur)
        return max_global
	```
	- 2-D case: O(n^3), brute-force O(n^4)
		- https://www.geeksforgeeks.org/maximum-sum-rectangle-in-a-2d-matrix-dp-27/
		```python
	    temp = [None] * ROW 
	    Sum = 0
	    start = [0] 
	    finish = [0]  
		for left in range(COL):
		    temp = [0] * ROW 
        	for right in range(left, COL):
            	for i in range(ROW): 
                	temp[i] += M[i][right]  
                    Sum = kadane(temp, start, finish, ROW)    
            		if Sum > maxSum: 
                		maxSum = Sum
                		finalLeft = left  
                		finalRight = right  
                		finalTop = start[0]  
                		finalBottom = finish[0]
		```
- Max sum <= K:
```python
sums = [sums[i]+matrix[i][r] for i in range(row)]
slist, num = [], 0
for i in range(row):
    num += sums[i]
    if num <= k: ans = max(ans, num)
    i = bisect.bisect_left(slist, num-k)
    if i != len(slist):
        ans = max(ans, num-slist[i])
    bisect.insort(slist, num)
```

## Subarray Satisfying...
- Typical questions:
	- LC-84: Largest Rectangle in Histogram (DP)
	- LC-992: Subarrays with K Different Integers

## Longest Subarray (DP)
- Typical questions:
	- LC-1027: Longest Arithmetic Sequence

## Array Permutation
- Typical questions:
	- **LC-932**: Beautiful Array (k with i < k < j such that A[k] * 2 = A[i] + A[j])
		- Thinking from odd/even;

## Array Jump
- Typical questions:
	- **LC-975**: Odd Even Jump (from A[i], odd jumps: jump to j with smallest A[j] s.t. A[j]>=A[i]; even jumps: jump to largest A[j] s.t. A[j]<=A[i])
		- Related to Count of Smaller Numbers After Self
		- DP with backup

## Array Move based on Height
- Typical questions:
	- LC-755: Pour Water (If the droplet would eventually fall by moving left, then move left; Otherwise, if the droplet would eventually fall by moving right, then move right; Otherwise, rise at it's current position.)

## 2D-Array, Matrix
- **LC-85**: Maximal Rectangle
- LC-221: Maximal Square

## Array Operation
- Typical questions:
	- LC-995: Minimum Number of K Consecutive Bit Flips
	- LC-1072: Flip Columns For Maximum Number of Equal Rows

## Inverse Pair Series
- Typical questions:
	- **LC-629**: K Inverse Pairs Array
		- Direct DP: O(nk^2), iterate dp[n][k] for k in [0..K]
		- Reduce the complexity by deduction between dp[n][k-1] and dp[n][k]
- Sorting-like:
	- LC-315: Count of Smaller Numbers After Self
	- LC-493: Reverse Pairs

## Sorting, Median, ...
- LC-324: Wiggle Sort II
	- Solution 1: sorting based
	- Solution 2: median based
- LC-1099: Two Sum Less Than K

## Stack
- LC-456. 132 Pattern

## Others
- LC-330: Patching Array
- Self in-place manipulation to avoid extra-space (notice array item range):
	- LC-442. Find All Duplicates in an Array
