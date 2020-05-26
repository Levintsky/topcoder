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

## Vector
```cpp
vector<Shape> vs;                  // No, don't - there is no room for a Circle or a Smiley
vector<Shape*> vps;                // better, but see §4.5.3
vector<unique_ptr<Shape>> vups;    // OK
```
- Member function:
- Iterators:
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
- Capacity:
```cpp
size() //Return size (public member function )
max_size() // Return maximum size (public member function )
resize() // Change size (public member function )
capacity() // Return size of allocated storage capacity (public member function )
empty() // Test whether vector is empty (public member function )
reserve() // Request a change in capacity (public member function )
shrink_to_fit() // Shrink to fit (public member function )
```
- Element access:
```cpp
operator[] // Access element (public member function )
T& at(int i); // Access element (public member function )
T& front(); // Access first element (public member function )
T& back(); // Access last element (public member function )
T* data(); // Access data (public member function )
```
- Modifiers:
```cpp
void assign(size_t s, T& val); // Assign vector content (public member function )
void push_back(const T& val); // Add element at the end (public member function )
void push_back(T&& val); // Add element at the end (public member function )
void pop_back() // Delete last element (public member function )
insert() // Insert elements (public member function )
iterator erase(const_iterator position); // Erase elements (public member function )
iterator erase (const_iterator first, const_iterator last);
swap() // Swap content (public member function )
clear() // Clear content (public member function )
emplace() // Construct and insert element (public member function )
emplace_back() // Construct and insert element at the end (public member function )
```

## List