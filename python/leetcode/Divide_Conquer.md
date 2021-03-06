# Divide and Conquer

## Sorting
- Quick-Sort
- Merge-Sort

## Sorting-like Algorithm
- Typical questions:
	- LC-315: Count of Smaller Numbers After Self
	- LC-493: Reverse Pairs

## Games
- **LC-843**: guess word;

## Binary Search
- Trial and Error for Solution:
	- LC-275: h-index;
	- LC-644: Max average subarray (trial and error)
	- LC-668: Kth largest product (trial and error)
	- LC-719: Find k-th smallest pair (trial and error)
	- LC-1014: separate numbers with min-sum;
- Find index, otherwise -1: LC 74, 704;
- Search target range: LC-34;
- Search Nearest: LC-475 heaters
- Rotated Array: LC-33, 81, 153, 154
- Median of two arrays: 4
- Find peak: 162
- Binary Search Library
	- bisect-left: return the first appearance, otherwise return the first one larger;
	- bisect: always return the first one larger;
```python
import bisect

# case 1: existing items
arr = [1, 1, 3, 5]
bisect.bisect_left(arr, 1) # return 0
bisect.bisect(arr, 1) # return 2

# case 2: non-existing items
# Both bisect and bisect_left returns the same
bisect.bisect_left(arr, 0) # return 0
bisect.bisect_left(arr, 4) # return 3
bisect.bisect_left(arr, 100) # return 4
```
	- Keep a list in sorted order:
```python
import bisect
kls = nums[:k]
kls.sort()
def update(num1, num2):
    # remove num1, add num2 to kls
    id1 = bisect.bisect_left(kls, num1)
    del kls[id1]
    bisect.insort(kls, num2)

    if k % 2 == 0:
        return sum(kls[k/2-1:k/2+1]) / 2.
    else:
        return float(kls[k/2])
```
	- Query:
```python
bisect.bisect_left(array, x)
bisect.bisect_right(array, x)
bisect.bisect(array, x) # same as bisect_right
```
	- Insert:
```python
bisect.insort_left(array, x)
bisect.insort_right(array, x)
bisect.insort(array, x)
```
- Find index, otherwise -1
```python
left, right = 0, n-1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target: return mid
    elif nums[mid] > target: right = mid - 1
    else: left = mid + 1
return -1
```
- problem 34, search target range
```python
i, j = 0, n-1
left, right = -1, -1
# search left
while i < j:
	mid = (i + j) // 2
    if A[mid] < target: i = mid + 1
    else: j = mid
if A[i] != target: return [left, right]
else: left = i
# search right
j = n-1
while i < j:
	mid = (i + j) // 2 + 1 # towards right?
	if A[mid] > target: j = mid - 1
    else: i = mid
right = j
return [left, right]
```
- Find item > than target
	- LC-35 (first item >= target, no duplicates)
```python
l, r = 0, n -1 
while l <= r:
    mid = (l + r) // 2
    if mid == target: return mid
    elif A[mid] > target: r = mid - 1
    else: l = mid + 1
return l
```
	- LC-744 (first item > target, with duplicates)
```python
# edge condition can't be handled
if target >= letters[-1]: return letters[0]
left, right = 0, n
while left < right:
    mid = (left + right) // 2
    if letters[mid] <= target: left = mid + 1
    else: right = mid
return letters[left]
```
- Search with function
```python
"""
find maximum ind in [0, n-1] s.t. A[ind] >= n-ind
"""
left, right = 0, n-1
while left <= right:
    mid = (left+right) // 2
    if A[ind] == n - ind: return A[ind]
    elif citations[mid] > (n-mid): right = mid - 1
    else: left = mid + 1
return n - right + 1
```
- 278 (find first bad, [true, true, ..., false])
```python
start = 1, n # included left, right
while start < end:
    mid = (end + start) // 2
    if not isBadVersion(mid): start = mid + 1
    else: end = mid            
return start
```
```python
while l < r:
    m = (l + r) // 2
    
    # count how many pairs <= m
    cnt, j = 0, 0
    for i in range(n):
        while j < n and nums[j] <= nums[i] + m:
            j += 1
        cnt += j - i - 1
```
- 1014 (separate numbers with min-sum)
```python
"""
find minimum number x in [min_, max_], s.t. f(x) <= D
x smaller, f(x) larger
can query f(x)
"""
start_, end = max(weights), sum(weights)
while start_ < end_:
    mid = (start_ + end_) // 2
    # print(start_, end_, mid, helper(mid), D)
    if helper(mid) <= D: end_ = mid
    else: start_ = mid + 1
return start_
```
- Rotated Array:
```python
# search in array without duplicate
# key: check target and nums[mid] on the same side or not
L, H = 0, len(nums)
while L < H:
    M = (L+H) // 2
    if target < nums[0] < nums[M]: # -inf
        L = M+1
    elif target >= nums[0] > nums[M]: # +inf
        H = M
    elif nums[M] < target:
        L = M+1
    elif nums[M] > target:
        H = M
    else:
        return M
return -1
```
