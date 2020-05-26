# Strings and Regular Expressions (Chap 9 of a Tour of C++)

## Overview
- Introduction
- Strings
	- string Implementation;
- String Views
- Regular Expressions
- Searching; Regular Expression Notation; Iterators
- Advice

## 9.2 Strings
```cpp
string a;
a.substr(i, n);
```
- Operator:
```cpp
os << s;
is >> s;
getline(is, s); // read a line
s.empty()
s.size()
s[n]
s1 + s2
s1 = s2 // deep copy
s1 == s2
<, <=, >, >=
```

## 9.4 Regular Expressions
- It specifies a pattern starting with two letters \w{2} optionally followed by some space \s* followed by five digits \d{5} and optionally followed by a dash and four digits −\d{4}
```cpp
regex pat {R"(\w{2}\s*\d{5}(−\d{4})?)"};
// U.S. postal code pattern: XXddddd-dddd and variants
```
