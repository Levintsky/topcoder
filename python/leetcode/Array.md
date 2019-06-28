# Array

## Subarray Sum
- Typical questions:
	- LC-363: Max Sum of Rectangle No Larger Than K
	- LC-862: Shortest Subarray with Sum at Least K
	- LC-1074: Number of Submatrices That Sum to Target
- Kadane's Algorithm to Maximum Sum Subarray Problem
	- https://www.youtube.com/watch?v=86CQq3pKSUw
	- 1-D case: O(n), brute-force O(n^2)
	```python
	def kadane(A):
	    max_cur = max_global = A[0]
	    for i in range(1, len(A)-1):
	        max_cur = max(A[i], A[i]+max_cur)
	        max_blobal = max(max_global, max_cur)
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

## Longest Array (DP)
- Typical questions:
	- LC-1027: Longest Arithmetic Sequence

## Array Permutation
- Typical questions:
	- 932: Beautiful Array (k with i < k < j such that A[k] * 2 = A[i] + A[j])
		- Thinking from odd/even;

## Array Jump
- Typical questions:
	- LC-975: Odd Even Jump (from A[i], odd jumps: jump to A[j]>=A[i]; even jumps: jump to A[j]<=A[i])

## Array Move based on Height
- Typical questions:
	- LC-755: Pour Water (If the droplet would eventually fall by moving left, then move left; Otherwise, if the droplet would eventually fall by moving right, then move right; Otherwise, rise at it's current position.)

## Array Operation
- Typical questions:
	- LC-995: Minimum Number of K Consecutive Bit Flips
	- LC-1072: Flip Columns For Maximum Number of Equal Rows

## Others
- LC-330: Patching Array
