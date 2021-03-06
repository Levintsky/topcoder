# Algorithms for Graph Theory

## BFS
- http://www.geeksforgeeks.org/breadth-first-traversal-for-a-graph/

## DFS
- http://www.geeksforgeeks.org/depth-first-traversal-for-a-graph/

## Dijkstra
- http://www.geeksforgeeks.org/greedy-algorithms-set-6-dijkstras-shortest-path-algorithm/

## Floyd Warshall Alg
- http://www.geeksforgeeks.org/dynamic-programming-set-16-floyd-warshall-algorithm/

## Prim
- http://www.geeksforgeeks.org/greedy-algorithms-set-5-prims-minimum-spanning-tree-mst-2/

## Kruskal
- http://www.geeksforgeeks.org/greedy-algorithms-set-2-kruskals-minimum-spanning-tree-mst/

## Topological Sorting
- http://www.geeksforgeeks.org/topological-sorting/

## Johnson's Algorithm
- http://www.geeksforgeeks.org/johnsons-algorithm/

## Articulation Points
- http://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/
```
 Naive O(V(V+E)):
  for every point:
   a) remove;
   b) see if graph remains connected (BFS or DFS);
   c) Add v back;
 O(V+E):
  DFS-tree:
   a vertex u is articulation point if one of the following two conditions is true.
    1) u is root of DFS tree and it has at least two children.
    2) u is not root of DFS tree and it has a child v such that no vertex in subtree rooted with v has a back edge to one of the ancestors (in DFS tree) of u.
  1. DFS, Maintains parent
  2. we maintain an additional array low[] which is defined as follows:
   low[u] = min(disc[u], disc[w]) 
   where w is an ancestor of u and there is a back edge from 
   some descendant of u to w.
```

## Bridges in a graph
- http://www.geeksforgeeks.org/bridge-in-a-graph/
```
 The condition for an edge (u, v) to be a bridge is, "low[v] > disc[u]".
```
