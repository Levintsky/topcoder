# C++ Prime Chap 3

## Namespace
```cpp
using namespace std::cin;
using namespace std::string;
```

## Vector
```cpp
vector<int> ivec(10, -1); // ten int elements, each initialized to -1
vector<int> ivec(10); // ten elements, each initialized to 0
v.empty()
v.size()
v.push_back(t)
v[n]
v1 = v2
v1 = {a, b, c}
v1 == v2
v1 != v2
<, <=, >, >=
```
- Iterator
```cpp
vector<int>::iterator it; // it can read and write vector<int> elements 
string::iterator it2; // it2 can read and write characters in a string 
vector<int>::const_iterator it3; // it3 can read but not write elements 
string::const_iterator it4; // it4 can read but not write characters

vector<int> v;
const vector<int> cv;
auto it1 = v.begin(); // it1 has type vector<int>::iterator 
auto it2 = cv.begin(); // it2 has type vector<int>::const_iterator
```
- Iterator operation
```cpp
iter + n
iter - n
iter += n
iter -= n
iter1 - iter2
>, >=, <, <=
```

## Array