# C++ Prime Chap 2

## Primitive Built-in Types
- 2.1 Primitive
```cpp
bool
char
wchar_t
char16_t
char32_t
short
int
long
long long
float
double
long double
```
- Unsigned for integers
```cpp
unsigned int
```
- Reference
```cpp
int *p;
int *&r = p; // reference pointer
```
	- Reference to const var must be const;
	- Const Reference could be non-const;
```cpp
const int a = 1024;
const int &r1 = a;
r1 = 42; // wrong
int &r2 = ci; // wrong!
const int &r2 = abc; // ok
r2 = 2; // wrong!
```

## Const
- Resource: https://www.cnblogs.com/wintergrass/archive/2011/04/15/2015020.html
- To share a const object among multiple files, you must define the variable as extern.
- usage 1: const on var;
```cpp
const int a = 10; // int const a=10 at compile time;
const int arr[3] = {1,2,3}; // same asint const arr[3] = {1,2,3};
const int i = get_size(); // ok: initialized at run time
const int k; // error
```
- usage 2: const on pointer and ref
```cpp
// const left of *, const var
// const right of *, cont pointer
const int* a = &var; // pointer to constant var
int const *a = &var; // a is a pointer to the constant variable
int* const a = &var; // a is a constant pointer to the (non-constant) variable
const int* const a = &var; // a constant pointer to the constant variable

int const &a=x;
const int &a=x;
int &const a=x;
```
- usage 3: const in function
```cpp
func(const T* a); func(const T& a);
const func(const T a);
const Rational operator*(const Rational& lhs, const Rational& rhs) {
	return Rational(lhs.numerator() * rhs.numerator(),
	lhs.denominator() * rhs.denominator());
}
// avoid the following case
Rational a,b;
Radional c;
(a*b) = c;
```
- usage 4: const in class
```cpp
class test {
 public:
  // 
  static int const gVar;

  // correct
  test(int size) : SIZE(size) {}

  // A "const function", denoted with the keyword const after a function declaration, makes it a compiler error for this class function to change a member variable of the class. However, reading of a class variables is ok inside of the function, but writing inside of this function will generate a compiler error.
  int getx() const {
  	x++; // wrong
  	return x; // OK
  }

 private:
  // correct from c++11
  const int SIZE = 100;
  int x;
}
```
- constexpr
```cpp
constexpr int mf = 20; // 20 is a constant expression
constexpr int limit = mf + 1; // mf + 1 is a constant expression
constexpr int sz = size(); // ok only if size is a constexpr function
```
	- for object: const can be compile/runtime const; constexpr always compile;
	- constexpr for function:
```cpp
#include <iostream>
#include <array>
using namespace std;

constexpr int foo(int i)
{
    return i + 5;
}

int main()
{
    int i = 10;
    std::array<int, foo(5)> arr; // OK
    
    foo(i); // Call is Ok
    
    // But...
    std::array<int, foo(i)> arr1; // Error  
}
```

## Define types
```cpp
struct xxx {

};
```
