# Advanced Data Structure

## Segment Tree 
- http://www.geeksforgeeks.org/segment-tree-set-1-range-minimum-query/
- RMQ (Range Minimum Query)
- Range Sum
- Lazy Propagation

## K-D Tree
- http://www.geeksforgeeks.org/k-dimensional-tree/
- Space Partitioning
- Classic Method:
     - cycles through the axes used to select the splitting planes;
     - select median of the points put into the subtree;

## Disjoint Set (Or Union-Find)
- http://www.geeksforgeeks.org/union-find/
    - find parent until -1
    - join the two

## Trie I (Insert and Search)
- http://www.geeksforgeeks.org/trie-insert-and-search/
    - Well-balanced BST: O(M logN)
    - Trie: O(M)

## Suffix Array
- http://web.stanford.edu/class/cs97si/suffix-array.pdf

## Range Minimum Query
- Square Root Decomposition
- http://www.geeksforgeeks.org/range-minimum-query-for-static-array/
- In case of static array,
    - Square Root Decomposition:
    - Divide into sqrt(n) each
    - O(sqrt(n)) space
    - each query takes O(sqrt(n)) time
- Sparse Table Algorithm
    - lookup[i][j]: min of range between index [i, 2^j]
- Alg:
    - If arr[lookup[0][3]] <=  arr[lookup[4][7]], 
      - then lookup[0][7] = lookup[0][3]
    - If arr[lookup[i][j-1]] <= arr[lookup[i+2j-1-1][j-1]]
      - lookup[i][j] = lookup[i][j-1]
    - If arr[lookup[0][3]] >  arr[lookup[4][7]], 
      - then lookup[0][7] = lookup[4][7]
    - Else 
      - lookup[i][j] = lookup[i+2j-1-1][j-1]

## Suffix automata
- http://www.geeksforgeeks.org/searching-for-patterns-set-5-finite-automata/
    - Naive
    - KMP
    - Rabin Karp

## Construction of Finite Automata
- http://www.geeksforgeeks.org/pattern-searching-set-5-efficient-constructtion-of-finite-automata/

## Find LCA in Binary Tree using RMQ
- http://www.geeksforgeeks.org/find-lca-in-binary-tree-using-rmq/
- Range Minimum Query (RMQ)
- Algorithm:
    - Do a Euler tour on the tree, and fill the euler, level and first occurrence arrays.
    - Using the first occurrence array, get the indices corresponding to the two nodes which will be the corners of the range in the level array that is fed to the RMQ algorithm for the minimum value.
    - Once the algorithm return the index of the minimum level in the range, we use it to determine the LCA using Euler tour array.
