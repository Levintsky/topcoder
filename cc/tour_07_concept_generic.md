# Concepts and Generic Programming (Chap 7 of a Tour of C++)

## Overview
- Introduction
- Concepts
	- Use of Concepts; Concept-Based Overloading; Valid Code; Definition of Concepts
- Generic Programming
	- Use of Concepts; Abstraction Using Templates
- Variadic Templates
	- Fold Expressions; Forwarding Arguments
- Template Compilation Model
- Advice

## 7.2 Overload

## 7.4 Variadic Template
- Suggested:
```cpp
template<typename T, typename ... Tail>
void print(T head, Tail... tail) {
     // what we do for each argument, e.g.,
     cout << head << ' ';
     print(tail...);
}
```
	- With **Compiled-time if**
```cpp
template<typename T, typename ... Tail>
void print(T head, Tail... tail) {
     cout << head << ' ';
     if constexpr(sizeof...(tail)> 0)
          print(tail...);
}
```
- Two common cases:
	- Variadic Template:
```cpp
template<typename... Args>
ostream &errorMsg(ostream &os, const Args&... rest) {
    return print(os, debug_rep(rest)...);
}
```
	- Initialization list:
```cpp
T { arg1, arg2, ... }
```