# Containers and Iterators

- A good summary of all the containers: https://blog.csdn.net/cywosp/article/details/7353754
```cpp
vector, list, queue, stack, deque, priority_queue,
// hash table
hash_multiset, hash_map, hash_multimap
```

## pair
```cpp
pair
```

## General Iterators
- http://www.cnblogs.com/chio/archive/2007/10/31/944122.html
- General members
```cpp
#include <iterator>
std::begin();
std::end();
```

## General Containers
- Capacity
```cpp
bool empty() const noexcept;
size_type size() const noexcept;
```
- General access:
```cpp
// auto find the one with matching type
std::get<string>(pair);

std::get<0>(std::pair<>); std::get<1>(std::pair<>);
std::get<>(std::tuple);
std::get<int>(std::array);
std::get<0>(std::variant);
```
- General modifiers:
```cpp
// both push_back and emplace_back available in vector, list, deque
// string only has push_back
void push_back(const value_type& val);
void push_back();
template<class... Args>
void emplace_back(Args&&... args);

// unordered_map, set, vector
clear();
```
- General iterators available in vector, array, unordered_map, set
```cpp
T* begin();
T* end();
T* cbegin(); // const iterator
T* cend();
```
- Other general functions:
```cpp
T* data();
```

## Hash Map Style
- General
```cpp
size_type max_size() const noexcept;

/* Element lookup */
iterator find ( const key_type& k );
const_iterator find ( const key_type& k ) const;
size_type count ( const key_type& k ) const;

/* Modifiers */
// generally, emplace(T1&&, T2&&)
template <class... Args>
pair<iterator, bool> emplace ( Args&&... args );
// insert(std::make_pair<T1, T2>(val1, val2));
pair<iterator,bool> insert ( const value_type& val );
erase(); // erase by key
clear();
swap();
```