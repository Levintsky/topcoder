# Binary Indexed Tree

## Resources
- https://www.topcoder.com/community/competitive-programming/tutorials/binary-indexed-trees/

## Basics
- Each node contains sum over all lower bit;
	- A number like xx100, will contain xx001, xx010, xx011, xx100
	- E.g., Arr[100] contains index 97, 98, 99, 100
```python
memo = {}

i = 1
n = 100

for i in range(1, n):
    ii = i
    
    # print('for', i)
    while ii <= n:
        if ii not in memo:
            memo[ii] = []
        memo[ii].append(i)
        ii += ii & (-ii)
        # print(ii)
print(memo)
```
- Visualization:\
	<img src="/python/leetcode/sp3-2.png" alt="drawing" width="400"/>
- Lowbit of x:
```python
lowbit(x) = x & (-x)
```
- Update: update along
```python
while i < n:
    array[i] += update
    i += lowbit(i)
```
- Query: sum of A[0..i], O(logn)
```python
res = 0
while i > 0:
    res += array[i]
    i -= lowbit(i)
```

## Applications
- Range Query Sum:
	- LC-307: 
	- LC-308: 2D
- Search
	- LC-315: count smaller after self;
	- LC-493: reverse pair;
