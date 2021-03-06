# Miscellaneous Algorithms

## Count Inversions (Using Merge Sort)
- http://www.geeksforgeeks.org/counting-inversions/
- Merge-Sort with a global accumulator

## Counting Inversions using BIT
- http://www.geeksforgeeks.org/count-inversions-array-set-3-using-bit/
```
 Binary Indexed Tree
 Each Index saved how many numbers smaller than itself
 Update from n .. 1
```

## Write a program to calculate pow(x,n)
- http://www.geeksforgeeks.org/write-a-c-program-to-calculate-powxn/
```
 Naive: O(n)
 Recursively: O(log n)
```

## Square root of an integer
- http://www.geeksforgeeks.org/square-root-of-an-integer/
```
 Binary Search
 Newton's Method
```

## Heavy Light Decomposition (HLD)
- http://www.geeksforgeeks.org/heavy-light-decomposition-set-1-introduction/
```
 Two queries:
  1) change(a, b): Update weight of the ath edge to b.
  2) maxEdge(a, b): Print the maximum edge weight on the path from node a to node b. For example maxEdge(5, 10) should print 25.
 HLD: coloring of tree edge, then segment tree
  1) change(u, v): O(log n)
  2) maxEdge(u, v): LCA, O(log n ^2)
```

## Rank of Matrix
- http://www.geeksforgeeks.org/program-for-rank-of-matrix/
- Row echelon form (like Gaussian Elimination)

## Gaussian Elimination to Solve Linear Equations
- http://www.geeksforgeeks.org/gaussian-elimination/

## Hungarian Algorithm
- https://en.wikipedia.org/wiki/Hungarian_algorithm
- https://zh.wikipedia.org/wiki/%E5%8C%88%E7%89%99%E5%88%A9%E7%AE%97%E6%B3%95
```
 	Clean bathroom	Sweep floors	Wash windows
 Armond		$2	$3	$3
 Francine	$3	$2	$3
 Herbert		$3	$3	$2
 Best Assignment: 2 + 2 + 2 = 6 $

 Bipartite Graph:
  Augmenting Path
```

## Link-Cut Algorithm
- http://www.cs.cmu.edu/~avrim/451f12/lectures/lect1009-linkcut.txt

## MO's Algorithm (Query Square Root Decomposition)
- http://www.geeksforgeeks.org/mos-algorithm-query-square-root-decomposition-set-1-introduction/
- http://blog.anudeep2011.com/mos-algorithm/
```
 O(n) -> O(sqrt(n))
```

## Factorial of a large number
- http://www.geeksforgeeks.org/factorial-large-number/
- multiply(res[], x)
- http://www.geeksforgeeks.org/biginteger-class-in-java/

## Russian Peasant (Multiply two numbers using bitwise operators)
- Given two integers, write a function to multiply them without using multiplication operator.
```
 The value of a*b is same as (a*2)*(b/2) if b is even, otherwise the value is same as ((a*2)*(b/2) + a)
```

## Catalan Number
- http://www.geeksforgeeks.org/program-nth-catalan-number/
- Catalan numbers are a sequence of natural numbers that occurs in many interesting counting problems like following.
```
 1) Count the number of expressions containing n pairs of parentheses which are correctly matched. For n = 3, possible expressions are ((())), ()(()), ()()(), (())(), (()()).
 2) Count the number of possible Binary Search Trees with n keys (See this) 
 3) Count the number of full binary trees (A rooted binary tree is full if every vertex has either two children or no children) with n+1 leaves.

Recursive:
 C(0) = 1
 C(n+1) = sum (C(i) * C(n-i))
```
