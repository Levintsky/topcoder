# Special Data-Structure

## Hash Map
- unordered_map: directly operate;
```cpp
unordered_map<T1, T2> m;
m[x1] = x2;
unordered_map<T1, vector<T2>> m;
m[x1].push_back(x2);
```

## Stack

## List

## Heap, Priority Queue
- Priority Queue is **max-heap** in C++;
```cpp
std::priority_queue<T> q;
void q.push(T);
void q.pop();
T q.top();
```