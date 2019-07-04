# BFS

## Array: Generate All...
- Typical questions:
	- **LC-301**: Remove Invalid Parentheses
		- BFS is much slower, but easier to implement

## Traversal
- Typical questions:
	- LC-310: Minimum Height Trees (find a node to make a tree with minimum height)
	- **LC-1036**: Escape a Large Maze (is it possible to go from source to target without being blocked)
		- key 1: two-way BFS;
		- key 2: no need to check really meet after 20,000 steps, if not blocked, meetable;

## BFS + Priority Queue
- Typical questions:
	- **LC-407**: Trapping Rain Water II
		- Visualize the problem first
		- Start with the lowest by heapq, keep a visit to avoid revisit
		- when add a low point (i, j, h) having water, add (i, j, h_max) and add the result by h_max - h
	- **LC-743**: Network Delay Time
		- Dijkstra
