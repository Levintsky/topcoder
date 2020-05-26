# Modularity (Chap 3 of a Tour of C++)

## Overview
- Introduction
- Separate Compilation
- Modules
- Namespaces
- Error Handling
- Exceptions; Invariants; Error-Handling Alternatives; Contracts; Static Assertions
- Function Arguments and Return Values
- Argument Passing; Value Return; Structured Binding”

## Separate Compilation
- .h file:
```cpp
// Vector.h:
class Vector {
public:
     Vector(int s);
	 double& operator[](int i);
     int size();
private:
     double* elem;      // elem points to an array of sz doubles
     int sz;
};
```
- .cpp file:
```cpp
// user.cpp:
#include "Vector.h"    // get Vector's interface
#include <cmath>       // get the standard-library math function interface including sqrt()

double sqrt_sum(Vector& v) {
     double sum = 0;
     for (int i=0; i!=v.size(); ++i)
           sum+=std::sqrt(v[i]);              // sum of square roots”
     return sum;
 }
```

## Module (not C++ standard)
```cpp
// file Vector.cpp:
module;  // this compilation will define a module
// ... here we put stuff that Vector might need for its implementation ...

export module Vector;  // defining the module called "Vector"

export class Vector {
public:
     Vector(int s);
     double& operator[](int i);
     int size();
private:
     double* elem;     // elem points to an array of sz doubles
     int sz;
};
Vector::Vector(int s)
     :elem{new double[s]}, sz{s}        // initialize members
{
}
double& Vector::operator[](int i) {
     return elem[i];
}
int Vector::size() {
     return sz;
}
export int size(const Vector& v) { return v.size(); }
```
- User.cpp
```cpp
// file user.cpp:
import Vector;         // get Vector's interface
#include <cmath>       // get the standard-library math function interface including sqrt()

double sqrt_sum(Vector& v) {
     double sum = 0;
     for (int i=0; i!=v.size(); ++i)
           sum+=std::sqrt(v[i]);        // sum of square roots
     return sum;
}
```

## Namespace

## Error Handling
- Exceptions
```cpp
double& Vector::operator[](int i) {
     if (i<0 || size()<=i)
           throw out_of_range{"Vector::operator[]"};
     return elem[i];
}
```
- Try, catch
```cpp
void f(Vector& v) {
     // ...
     try{ // exceptions here are handled by the handler defined below

          v[v.size()] = 7; // try to access beyond the end of v
     } catch (out_of_range& err) {   // oops: out_of_range error
          // ... handle range error ...
          cerr << err.what() << '\n';
     }
     // ...
}
```
- Contracts, alert
```cpp
void f(const char* p) {
     assert(p!=nullptr);  // p must not be the nullptr
     // ...
}
```
- Static assert: compile-time
```cpp
constexpr double C = 299792.458;                       // km/s

void f(double speed)
{
     constexpr double local_max = 160.0/(60*60);       // 160 km/h == 160.0/(60*60) km/s

     static_assert(speed<C,"can't go that fast");      // error: speed must be a constant
     static_assert(local_max<C,"can't go that fast");  // OK
     // ...
}
```

## Arguments
- Pass by value/arguments
- Return
```cpp
auto mul(int i, double d) { return i*d; }       // here, "auto" means "deduce the return type
```
