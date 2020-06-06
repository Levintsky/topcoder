# Templates (Chap 6 of a Tour of C++)

## Overview
- Introduction
- Parameterized Types
	- Constrained Template Arguments; Value Template Arguments; Template Argument Deduction
- Parameterized Operations
	- Function Templates; Function Objects; Lambda Expressions
- Template Mechanisms
	- Variable Templates; Aliases; Compile-Time if
- Advice
  - Suggest not split declaration and implementation into .h and .cc;

## 6.1 Implementation
- Declaration and definition all in header file (recommended)
- Separate in .cpp file? explicit
  - .h declaration only
```cpp
// foobar.h
template <typename T>
class foobar {
public:
    foobar() : data() {
        data = new T;
    }
    ~foobar() {
        delete data;
    }
    T* get();
private:
    T* data;
};
```
  - .cpp file
```cpp
// foobar.cpp
#include "foobar.h"

template<typename T>
T* foobar<T>::get() {
    return this->data;
}
template class foobar<int>;
```

## 6.2 Parametrized Types
```cpp
template<typename T>
class Vector {
private:
     T* elem;  // elem points to an array of sz elements of type T
     int sz;
public:
     explicit Vector(int s);          // constructor: establish invariant, acquire resources
     ~Vector() { delete[] elem; }     // destructor: release resources

     // ... copy and move operations ...

     T& operator[](int i);                     // for non-cost Vectors
     const T& operator[](int i) const;         // for const Vectors (§4.2.1)
     int size() const { return sz; }
};
```
- Constrained type (C++20)
```cpp
Vector<int> v1;     // OK: we can copy an int
Vector<thread> v2;  // error: we can't copy a standard thread (§15.2)
```
- Value template argument
```cpp
template<typename T, int N>
struct Buffer {
     using value_type = T;
     constexprint size() { return N; }
     T[N];
     // ...
};

Buffer<char,1024> glob;  // global buffer of characters (statically allocated)”
```
- Template Argument Deduction
```cpp
pair<int,double> p = {1,5.2};
auto p = make_pair(1,5.2);    // p is a pair<int,double>

auto p = new Vector{1,2,3};   // p points to a Vector<int>
Vector<int> v3(1);  // here we need to be explicit about the element type
```

## 6.3 Parameterized Operations
- function template:
```cpp
template<typename T>
T add(T& a, T& b);
// Compiler can infer type
int x = add(2, 3); // correct 
float y = add(2., 3.); //correct
add(2, 3.); // error, can't infer type
add<float>(2, 3.); // correct
```
- function object/functor
```cpp
template<typename T>
class Less_than {
     const T val;   // value to compare against
public:
     Less_than(const T& v) :val{v} { }
     bool operator()(const T& x) const { return x<val; } // call operator
};

Less_than lti {42};                // lti(i) will compare i to 42 using < (i<42)
Less_than lts {"Backus"s};         // lts(s) will compare s to "Backus" using < (s<"Backus")
Less_than<string> lts2 {"Naur"};   // "Naur" is a C-style string, so we need <string> to get the right <
```
- Lambda expression:
	- The notation 
```cpp
[&](int a){ return a<x;}
```
	is called a lambda expression.
	- It generates a function object exactly like 
```cpp
Less_than<int>{x}
```
	The [&] is a capture list specifying that all local names used in the lambda body (such as x) will be accessed through references.
	- Had we wanted to “capture” only x, we could have said so: [&x].
	- Had we wanted to give the generated object a copy of x, we could have said so: [=x].
	- Capture nothing is [ ], capture all local names used by reference is [&], and capture all local names used by value is [=].
```cpp
void f(const Vector<int>& vec, const list<string>& lst, int x, const string& s) {
     cout << "number of values less than " << x
          << ": " << count(vec,[&](int a){ return a<x; })
          << '\n';
     cout << "number of values less than " << s
          << ": " << count(lst,[&](const string& a){ return a<s; })
          << '\n';
}
```

## Specialization
- Full:
```cpp
template <>
class A<int, double>{
    int data1;
    double data2;
};
template <>
int max(const int lhs, const int rhs){   
    return lhs > rhs ? lhs : rhs;
}
```
- Ambiguity, specify;
```cpp
template <class T>
void f(){ T d; }

template <>
void f(){ int d; } // could be wrong (ambiguity)

template <>
void f<int>(){ int d; } // correct
```
- Partial: only allowed in classes, not in functions!!!
```cpp
template <class T2>
class A<int, T2>{
    ...
};
```
  - In functions, wrong!
```cpp
template <class T1, class T2>
void f(){}

template <class T2>
void f<int, T2>(){}
```

## Template Mechanism
- Language support required:
	- Values dependent on a type: variable templates (§6.4.1).
	- Aliases for types and templates: alias templates (§6.4.2).
	- A compile-time selection mechanism: if constexpr (§6.4.3).
	- A compile-time mechanism to inquire about properties of types and expressions: requires-expressions (§7.2.3).
- Alias:
```cpp
using size_t = unsigned int;

template<typename T>
class Vector {
public:
     using value_type = T;
     // ...
};
```
- Compile-time if
```cpp
template<typename T>
void update(T& target) {
     // ...
     if constexpr(is_pod<T>::value)
          simple_and_fast(target); // for "plain old data"
     else
          slow_and_safe(target);
     // ...
}
```

## Examples
- template class
  - default template
```cpp
template <class T, class F=less<T>>
```
- template function in a template class
```cpp
template <T>
class A {
  template<S>
  func(xxx) {}
};
A<T> a;
A<T> *b;
a.template func(xxx);
b->template func(xxx);
```
- template in template
```cpp
template<template<class> class T, class S>
void f(T<S> value); // template in template function

template<template<class> class T>
class ABC {
  template<S>
  ABC(T<S>);
};
```