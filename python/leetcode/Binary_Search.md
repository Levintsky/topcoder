# Binary Search Summary

## Binary Search Library
- bisect-left: return the first appearance, otherwise return the first one larger
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

## Find index, otherwise -1
- Typical questions:
    - problem 74, 704
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

## Find item > than target
- 35 (first item >= target, no duplicates)
```python
l, r = 0, n -1 
while l <= r:
    mid = (l + r) // 2
    if mid == target: return mid
    elif A[mid] > target: r = mid - 1
    else: l = mid + 1
return l
```
- 744 (first item > target, with duplicates)
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

## Search Nearest
- 475 heaters

## Search with function
- 275 (h-index)
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
- 644 Max average subarray (trial and error)
- 668 Kth largest product (trial and error)
- 719 Find k-th smallest pair (trial and error)
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

## More Fancy
- Rotated Array: 33, 81, 153, 154
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
- Find peak: 162
- Median of two arrays: 4