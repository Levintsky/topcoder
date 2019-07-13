# Count Digits in an Array

## Count Repeat/Unique
- LC-600: Non-negative Integers without Consecutive Ones
- LC-1012: numbers With Repeated Digits (Hard)
	- Always easier to find unique
	- Like 8765, we need to find patterns:
		- x, xx, xxx (9 x 9 x 8 x ...)
		- 1xxx - 7xxx
		- 80xx - 86xx
		- 870x - 875x
		- 8760 - 8765
- LC-1015: Numbers With 1 Repeated Digit
- LC-357: number with unique digits (Specific case of 1012)
- LC-788: rotate digit (digits in set([0, 1, 8, 2, 5, 6, 9]))
- LC-902: Numbers At Most N Given Digit Set
- LC-1088: Confusing Number II
- LC-660: Remove 9

## Count a Specific Digit
- LC-233: Same as 1067, Count 1;
	- https://leetcode.com/articles/number-of-digit-one/
	- Count by position:
		- 1s: xx1, xx1, ...
		```python
		n // 10 + (n % 10 != 0)
		```
		- 10s: x1x, x1x, ...
		```python
		# 1600-1609: 0 1s
		# 1610-1619: n % 100 - 10 + 1
		# >=1620, containing all 10 [1610, 1611, ..., 1619] numbers
		(n // 100) * 10 + min(max(n % 100 - 10 + 1, 0), 10)
		```
		- 100s: x1xx, x1xx, ...
		```python
		(n // 100) * 10 + min(max(n % 1000 - 100 + 1, 0), 100)
		```
- LC-1067: between Low and High, how many times a specific digit appears;
	- For digit [1..9] same as Problem-233
	- For digit 0
		- Case 1: last digit such as xxx0 (not influenced)
		- Case 2: middle digit x0xx (like 2038, when count x0xx)
		```python
		cnt -= 100
		cnt += min(n % 1000 + 1, 100)
		```
		- Case 3: First digit 0xxx (not influenced)

## Count Sequentially
- LC-400: Nth Digit (find n-th digit along 1,2,..,10,..)