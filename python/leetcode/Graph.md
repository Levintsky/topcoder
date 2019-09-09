# Graph

## Euler Graph
- Typical questions:
	- LC-332: Reconstruct Itinerary

## Problem Seen as a Graph
- Typical questions:
	- 440. K-th Smallest in Lexicographical Order (Hard)

## Shortest Path
- BFS + Priority Queue:
	- LC-743: Network Delay Time
	- LC-787: Cheapest Flights Within K Stops

## Topological Sorting
- Algorithm
	- A memo to record in-degree:
	- A memo to record c: next-char sets
	- Keep a zero in-degree set, update
- Typical questions:
	- LC-269: Alien Dictionary

## Critical Point and Edge (Articulation Point, Bridge)
- **LC-1192**: Critical Connections in a Network
	- Brute force O(V(V+E))
	- DFS with memo: recording back edge, O(V+E)