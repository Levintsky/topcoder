# C++ Data Structures Study

## String:
- Basics
```cpp
#include <string>
string a;
// Access
a[3] = 'c';
cout << a.at(i);
// capacity
a.empty(); a.size();
a.length();
// iterators
a.begin(); a.end();
// modifiers
a.clear();
a.insert(index, "abc");
// compare
str1.compare(str2) != 0;
a += b;
// find
```
- Literals
```cpp
" (unescaped_character|escaped_character)* "
R"" // used to avoid any escaping
```

## auto type
```cpp
auto a = 3;
```

## Type Conversion:
-- Static Cast is used to (1) cast void* to other type; (2) regular type conversion; (3) avoid ambiguity;
```cpp
static_cast<T>(object);
```
-- Dynamic cast is used to cast between derived and base class;
```cpp
Derived* dynamic_cast<Derived*>(basic_ptr);
Derived2* pd2 = static_cast<Derived2*>(derived1_ptr);
```
-- Reinterpret cast: conversion between pointer and int;
```cpp
reinterpret_cast<T>(object);
```
-- Change something const to volatile
```cpp
const_cast<T>(object);

const B b1;
b1.m_iNum = 100; //comile error
B b2 = const_cast<B>(b1);
b2.m_iNum = 200; //fine
```

## rtti
- runtime type info
```cpp
#include <typeinfo>
int i;
// typeid() is an operator
typeid(i).name();
```
