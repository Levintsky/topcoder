# Algorithms (Chap 12 of a Tour of C++)

## Overview
- Introduction
- Use of Iterators
- Iterator Types
- Stream Iterators
- Predicates
- Algorithm Overview
- Concepts
- Container Algorithms
- Parallel Algorithms
- Advice

## Introduction
```cpp
void f(vector<Entry>& vec, list<Entry>& lst) {
     sort(vec.begin(),vec.end());                      // use < for order
     unique_copy(vec.begin(),vec.end(),lst.begin());   // don't copy adjacent equal elements
}
```

## Iterator
```cpp
list<Element>::iterator
```

## Stream Iterator
