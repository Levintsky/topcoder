# Containers (Chap 11 of a Tour of C++)

## Overview
- Introduction
- vector
	- Elements; Range Checking
- list
- map
- unordered_map
- Container Overview
- Advice

## Vector, List
- Shared by vector and list
	- **Iterators**:
```cpp
begin() // Return iterator to beginning (public member function )
end() // Return iterator to end (public member function )
rbegin() // Return reverse iterator to reverse beginning (public member function )
rend() // Return reverse iterator to reverse end (public member function )
cbegin() // Return const_iterator to beginning (public member function )
cend() // Return const_iterator to end (public member function )
crbegin() // Return const_reverse_iterator to reverse beginning (public member function )
crend() // Return const_reverse_iterator to reverse end (public member function )
```
	- **Capacity**:
```cpp
bool empty(); // Test whether vector is empty (public member function )
size_t size() const; //Return size (public member function )
max_size() // Return maximum size (public member function )
```
	- **Access**:
```cpp
T& front(); // Access first element (public member function )
T& back(); // Access last element (public member function )
```
	- **Modifiers**:
```cpp
void clear() noexcept; // Clear content (public member function )
iterator insert(iterator pos, const T& val); // Insert elements (public member function )
iterator erase (const_iterator first, const_iterator last);
iterator emplace(const_iterator pos, Args&&... args); // Construct and insert element (public member function )
iterator erase(const_iterator position); // Erase elements (public member function )
void push_back(const T& val); // Add element at the end (public member function )
void push_back(T&& val); // Add element at the end (public member function )
void emplace_back(Args&&... args) // Construct and insert element at the end (public member function )
void pop_back(); // Delete last element (public member function )
```
- Vector
```cpp
vector<Shape> vs;                  // No, don't - there is no room for a Circle or a Smiley
vector<Shape*> vps;                // better, but see §4.5.3
vector<unique_ptr<Shape>> vups;    // OK
```
	- Member function:
	- Capacity:
```cpp
resize() // Change size (public member function )
capacity() // Return size of allocated storage capacity (public member function )
reserve() // Request a change in capacity (public member function )
shrink_to_fit() // Shrink to fit (public member function )
```
	- Element access:
```cpp
T& operator[](size_type pos); // Access element (public member function )
T& at(int i); // Access element (public member function )
T* data(); // Access data (public member function )
```
	- Modifiers:
```cpp
void assign(size_t s, T& val); // Assign vector content (public member function )
void swap(vector& other); // Swap content (public member function )
```
- List
	- Modifiers:
```cpp
void push_front(const T& value);
void push_front(T&& value);
void emplace_front(Args&&... args);
reference emplace_front( Args&&... args );
```

## Map, Unordered map
- Shared between map and unordered_map
	- Element type:
```cpp
std::pair<const Key, T>
```
	- Iterator:
```cpp
begin() // Return iterator to beginning (public member function )
end() // Return iterator to end (public member function )
cbegin() // Return const_iterator to beginning (public member function )
cend() // Return const_iterator to end (public member function )
```
	- **Capacity**:
```cpp
bool empty(); // Test whether vector is empty (public member function )
size_t size() const; //Return size (public member function )
max_size() // Return maximum size (public member function )
```
	- Modifiers:
```cpp
clear();
insert();
emplace();
erase();
swap();
merge();
```
	- Lookup:
```cpp
size_type count(const Key& key) const;
iterator find( const Key& key);
```
- Map specific:
```cpp
template<
    class Key,
    class T,
    class Compare = std::less<Key>,
    class Allocator = std::allocator<std::pair<const Key, T> >
> class map;
```
	- Access:
```cpp
T& at(const Key& key);
T& operator[](const Key& key);
T& operator[](Key&& key);
```
	- Iterator:
```cpp
rbegin() // Return reverse iterator to reverse beginning (public member function )
rend() // Return reverse iterator to reverse end (public member function )
crbegin() // Return const_reverse_iterator to reverse beginning (public member function )
crend() // Return const_reverse_iterator to reverse end (public member function )
```
	- **Capacity**:
	- Modifier:
	- Lookup:
```cpp
iterator lower_bound(const Key& key);
iterator upper_bound(const Key& key);
```
- Unordered-map specific:
	- Bucket interface:
```cpp
bucket_count() // returns the number of buckets
max_bucket_count() // returns the maximum number of buckets
bucket_size() // returns the number of elements in specific bucket
bucket()
```
	- Hash policy:
```cpp
hash_function()
key_eq()
```

## Stack
```cpp
bool empty() // Test whether container is empty (public member function )
int size() // Return size (public member function )
T top() // Access next element (public member function )
void push(T& item) // Insert element (public member function )
void emplace(T& item); // Construct and insert element (public member function )
void pop(); // Remove top element (public member function )
void swap(stack& x);
```

## Overview
```cpp
vector<T> // A variable-size vector (§11.2)
list<T> // A doubly-linked list (§11.3)
forward_list<T> // A singly-linked list
deque<T> // A double-ended queue
set<T> // A set (a map with just a key and no value)
multiset<T> // A set in which a value can occur many times
map<K,V> // An associative array (§11.4)
multimap<K,V> // A map in which a key can occur many times
priority_queue<T>
queue<T>
stack<T>
unordered_map<K,V> // A map using a hashed lookup (§11.5)
unordered_multimap<K,V> // A multimap using a hashed lookup
unordered_set<T> // A set using a hashed lookup
unordered_multiset<T> // A multiset using a hashed lookup
```
