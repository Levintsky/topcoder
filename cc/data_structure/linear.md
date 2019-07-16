# Linear DS

## Array
- array: no size change
```cpp
std::array<T, kN> arr; // can't change size
```

## Vector
```cpp
#include <vector>
std::vector<T> arr;

// void push_back(const value_type& val);
arr.push_back(val);
// template<class... Args>
// void emplace_back(Args&&... args);

// insert(int index, T& );
arr.insert(i, val);

resize(int );
```

## Linked List
- List: double-linked list
```cpp
#include <list>
list<T> a;
// access
a.top(); a.top() -= 5;
a.back();
# Modifier
a.insert(iterator pos, const T& value);
a.push_back(const T& value);
a.push_back(T&& value);
```
- slist: single-linked list (queue)
```cpp
slist<T> a;
```

## stack and queue
- General
```cpp
/* Modifier */
// e.g. a.push(5);
void push (const value_type& val);
void push (value_type&& val);
template <class... Args> void emplace (Args&&... args);

void pop();
```
- Stack: LIFO
```cpp
#include <stack>
stack<int> a;

// Access
T& top(); // a.top() -= 5;
```
- Queue: FIFO (queue, deque)
```cpp
#include <queue>
queue<T> my_q;
deque<T> my_q;

// Access: front(), back()
// e.g. myqueue.front() -= myqueue.back();
// first item
reference& front();
const_reference& front() const;
// last item
reference& back();
const_reference& back() const;
```

## Search
- Binary search only return true/false!
```cpp
bool res = std::binary_search(hay.begin(), hay.end(), item);
```