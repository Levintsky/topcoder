# System Design

## Stack
- **LC-155**: Min Stack
- LC-225: Implement Stack using Queues
- LC-232: Implement Queue using Stacks

## Queue
- LC-239: Sliding Window Maximum

## Moving Statistics
- LC-295: Find Median from Data Stream
	- Only add, no remove
	- Balanced BST, RB-Tree
	- bisect also works
	- Two heaps work: no removal
- LC-480: Sliding Window Median
	- **Multiset**
	- **No free method to update median, use an iterator**!
- Moving Max: decreasing deque;
	- Key insight: if i < j and A[i] < A[j], then A[i] will never be selected;
	- LC-239: moving maximum;

## Iterator
- LC-173: Binary Search Tree Iterator (level-order)
	- **Keep the stack**;
	- Traverse **iteratively**;
- LC-251: Flatten 2D Vector
- LC-281: Zigzag Iterator
- LC-284: Peeking Iterator
- LC-341: Flatten Nested List Iterator

## Segment Tree/Binary Index Tree
- LC-307: Range Sum Query - Mutable
- LC-493: Reverse Pairs

## Invert Indexing
- LC-432: All O(1) Data Structure

## Cache
- **LC-146**: LRU Cache
	- Double linked-list + Hash-table;
	<img src="/python/leetcode/images/lru-cache.png" alt="drawing" width="500"/>

- LC-460: LFU Cache

## Multithreading
- **LC-1114**: Print in Order
