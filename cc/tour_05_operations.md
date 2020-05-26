# Essential Operations (Chap 5 of a Tour of C++)

## Overview
- Introduction
	- Essential Operations; Conversions; Member Initializers
- Copy and Move
	- Copying Containers; Moving Containers
- Resource Management
- Conventional Operations
	- Comparisons; Container Operations; Input and Output Operators; User-Defined Literals; swap(); hash<>
- Advice

## Introduction
```cpp
class X {
public:
     X(Sometype);            // "ordinary constructor": create an object
     X();                    // default constructor
     X(const X&);            // copy constructor
     X(X&&);                 // move constructor
     X& operator=(const X&); // copy assignment: clean up target and copy
     X& operator=(X&&);      // move assignment: clean up target and move
     ~X();                   // destructor: clean up
     // ...
};
```
- Not to be generated: =delete:
```cpp
class Shape {
public:
     Shape(const Shape&) =delete;            // no copy operations
     Shape& operator=(const Shape&) =delete;
     // ...
};
void copy(Shape& s1, const Shape& s2) {
     s1 = s2;  // error: Shape copy is deleted
}
```

## Copy and move:
```cpp
Vector f() {
     Vector x(1000);
     Vector y(2000);
     Vector z(3000);
     z = x;              // we get a copy (x might be used later in f())
     y = std::move(x);   // we get a move (move assignment)
     // ... better not use x here ...
     return z;           // we get a move
}
```

## Resource Management
- RAII (Resource Acquisition Is Initialization)
- In the C++ standard library, RAII is pervasive:
	- memory (string, vector, map, unordered_map, etc.);
	- files (ifstream, ofstream, etc.), threads (thread);
	- locks (lock_guard, unique_lock, etc.)
	- general objects (through unique_ptr and shared_ptr).

## Conventional Operations
- Comparisons: ==, !=, <, <=, >, and >= (§5.4.1)
- Container operations: size(), begin(), and end() (§5.4.2)
- Input and output operations: >> and << (§5.4.3)
- User-defined literals (§5.4.4)
- swap() (§5.4.5)
- Hash functions: hash<> (§5.4.6)
