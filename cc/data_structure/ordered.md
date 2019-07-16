# Ordered Non-linear DS

## Balanced BST
```cpp
set, multiset, multimap;
```
- Set:
```cpp
#include <set>
set<int> a;
```
- multiset (allow duplicate keys)
- same thing, but implemented in hash-table:
```cpp
hash_set
hash_multiset
hash_map
hash_multimap
```
- Map:

## Priority Queue
- max-heap in c++!
```cpp
#include <queue>
std::priority_queue<T> a;

// priority queue with compare function
priority_queue<int, vector<int>, std::greater<int> > q;

// Access
T& top(); // a.top() -= 5;
```