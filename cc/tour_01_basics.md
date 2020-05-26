# Basics (Chap 1 of a Tour of C++)

## Overview
- Introduction
- Programs
- Hello, World!
- Functions
- Types, Variables, and Arithmetic
- Arithmetic; Initialization
- Scope and Lifetime
- Constants
- Pointers, Arrays, and References
- The Null Pointer
- Tests
- Mapping to Hardware
	- Assignment; Initialization
- Advice

## 1.4 Types
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
- Arithmetic
```cpp
x+y     // plus
+x      // unary plus
x−y     // minus
-x      // unary minus
x*y     // multiply
x/y     // divide
x%y     // remainder (modulus) for integers
```
	- Comparison
```cpp
x==y     // equal
x!=y     // not equal
x<y      // less than
x>y      // greater than
x<=y     // less than or equal
x>=y     // greater than or equal”
```
	- Logical
```cpp
x&y      // bitwise and
x|y      // bitwise or
x^y      // bitwise exclusive or
~x       // bitwise complement
x&&y     // logical and
x||y     // logical or
!x       // logical not (negation)”
```
	- Specific
```cpp
x+=y     // x = x+y
++x      // increment: x = x+1
x−=y     // x = x-y
−−x      // decrement: x = x-1
x*=y     // scaling: x = x*y
x/=y     // scaling: x = x/y
x%=y     // x = x%y”
```
	- Initialization
```cpp
double d1 = 2.3;                 // initialize d1 to 2.3
double d2 {2.3};                 // initialize d2 to 2.3
double d3 = {2.3};               // initialize d3 to 2.3 (the = is optional with { ... })
complex<double> z = 1;           // a complex number with double-precision floating-point scalars
complex<double> z2 {d1,d2};
complex<double> z3 = {d1,d2};    // the = is optional with { ... }
vector<int> v {1,2,3,4,5,6};     // a vector of ints”

int i1 = 7.8;        // i1 becomes 7 (surprise?)
int i2 {7.8};        // error: floating-point to integer conversion”
```
	- Auto: deduced from initializer:
```cpp
auto b = true;       // a bool
auto ch = 'x';       // a char
auto i = 123;        // an int
auto d = 1.2;        // a double
auto z = sqrt(y);    // z has the type of whatever sqrt(y) returns
auto bb {true};      // bb is a bool
```

## 1.5 Scope and Lifetime

## 1.6 Constants
- const and constexpr:
	- const: can be computed at run time;
	- constexpr: compile-time; function must also be constexpr type:
```cpp
constexpr double square(double x) { return x*x; }
```
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

## 1.7 Pointers, Arrays, Reference
- Pointer:
```cpp
double* pt = nullptr;
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

## 1.8 Control Flow
- if
```cpp
if (x == 100) {
	cout << "x" << endl;
} else if (x = 90) {
	cout << x << endl;
} else {
	cout << "default" << endl;
}
```
- switch
```cpp
int a;
switch(a) {
  case 1:
    cout << '1'; // prints "1",
    break;
  case 2:
    cout << '2'; // then prints "2"
    break;
  default:
    break;
}
```
- while
```cpp
while (n > 0) {
	cout << n << endl;
	--n;
}
```
- do while
```cpp
do {
	cout << "Enter text: " << endl;
	cout << x;
} while (x);
```
- for
```cpp
for (int i = 0; i < 10; ++i) {
	cout << i << endl;
}
```