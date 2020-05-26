# Classes (Chap 4 of a Tour of C++)

## Overview
- Introduction
- Concrete Types
- An Arithmetic Type; A Container; Initializing Containers
- Abstract Types
- Virtual Functions
- Class Hierarchies
- Benefits from Hierarchies; Hierarchy Navigation; Avoiding Resource Leaks
- Advice

## 4.2 Examples
- Arithmetic
```cpp
class complex {
     double re, im; // representation: two doubles
public:
     complex(double r, double i) :re{r}, im{i} {}    // construct complex from two scalars
     complex(double r) :re{r}, im{0} {}              // construct complex from one scalar
     complex() :re{0}, im{0} {}                      // default complex: {0,0}

     double real() const { return re; }
     void real(double d) { re=d; }
     double imag() const { return im; }
     void imag(double d) { im=d; }

     complex& operator+=(complex z) {
         re+=z.re;         // add to re and im
         im+=z.im;
         return *this;     // and return the result
     }
     complex& operator−=(complex z) {
         re−=z.re;
         im−=z.im;
         return *this;
     }

     complex& operator*=(complex);    // defined out-of-class somewhere
     complex& operator/=(complex);    // defined out-of-class somewhere
};
```
- Container
```cpp
class Vector {
public:
     Vector(int s) :elem{new double[s]}, sz{s}     // constructor: acquire resources
     {
          for (int i=0; i!=s; ++i)      // initialize elements
                elem[i]=0;
     }
     Vector(std::initializer_list<double>);     // initialize with a list of doubles
     // ...

     ~Vector() { delete[] elem; }                  // destructor: release resources

     void push_back(double);
     double& operator[](int i);
     int size() const;
private:
     double* elem;     // elem points to an array of sz doubles
     int sz;
};
```

## Hierarchies
- Base class;
```cpp
class Shape {
public:
     virtual Point center() const =0;     // pure virtual
     virtual void move(Point to) =0;

     virtual void draw() const = 0;       // draw on current "Canvas"
     virtual void rotate(int angle) = 0;

     virtual ~Shape() {}                  // destructor
     //...
};
```
- Derived class:
```cpp
class Smiley : public Circle {  // use the circle as the base for a face
public:
     Smiley(Point p, int rad) : Circle{p,r}, mouth{nullptr} { }

     ~Smiley()
     {
          delete mouth;
          for (auto p : eyes)
                delete p;
     }

     void move(Point to) override;

     void draw() const override;
     void rotate(int) override;

     void add_eye(Shape* s)
     {
          eyes.push_back(s);
     }
     void set_mouth(Shape* s);
     virtual void wink(int i);     // wink eye number i

     // ...

private:
     vector<Shape*> eyes;          // usually two eyes
     Shape* mouth;
};
```
- To call a specific derived member function: **dynamic_cast**
```cpp
Shape* ps {read_shape(cin)};

if (Smiley* p = dynamic_cast<Smiley*>(ps)) { // ... does ps point to a Smiley? ...
     // ... a Smiley; use it
} else {
     // ... not a Smiley, try something else ...
}
```
- Avoid resource leaks:
  - **delete** required for naked pointer;
```cpp
void user(int x) {
     Shape* p = new Circle{Point{0,0},10};
     // ...
     if (x<0) throw Bad_x{};   // potential leak
     if (x==0) return;         // potential leak
     // ...
     delete p;
}
```
  - **unique_ptr**
```cpp
unique_ptr<Shape> read_shape(istream& is) {
     // read shape header from is and find its Kind k
     switch (k) {
     case Kind::circle:
          // read circle data {Point,int} into p and r
          return unique_ptr<Shape>{new Circle{p,r}};       // §13.2.1
     // ...
}

void user() {
     vector<unique_ptr<Shape>> v;
     while (cin)
          v.push_back(read_shape(cin));
     draw_all(v);               // call draw() for each element
     rotate_all(v,45);          // call rotate(45) for each element
}// all Shapes implicitly destroyed
```

## Constructors
- A good article (http://www.cnblogs.com/chio/archive/2007/10/20/931043.html):
- The **explicit** specifier specifies that a constructor or conversion function (since C++11) doesn't allow implicit conversions or copy-initialization. It may only appear within the decl-specifier-seq of the declaration of such a function within its class definition.
```cpp
struct A {
  A(int) { }
  explicit A(int, int) {}
};
A a1 = 1; // OK
A a2 = {1, 2}; // error

// example 2
class MyClass {
public:
  explicit MyClass( int num );
};
MyClass obj = 10; // error, b/c explit
// otherwise, will be MyClass tmp(10); obj = tmp;
```

## private, protected and public
- The difference between private and protected comes into play only within classes derived from the base class;
- Members of a derived class can access protected members of a base class directly, but they can't directly access private members of the base class.
```cpp
class Base {
 public:
  int publicMember; // Everything that is aware of Base is also aware that Base contains publicMember.
 protected:
  int protectedMember; // Only the children (and their children) are aware that Base contains protectedMember.
 private:
  int privateMember; // No one but Base is aware of privateMember.
};
```
- Inheritance: if not specified, regard as private inheritance
```cpp
public Base {
  public: int a;
  protected: int b;
  private: int c;
}

// a public, b protected, c invisible
class derived1 : public base {}

// a protected, b protected, c invisible
class derived2 : protected base {}

// a private, b private, c invisible
class derived3 : private base {}
```
- Override:
```cpp
struct A {
    virtual void foo();
    void bar();
};
 
struct B : A {
    void foo() const override; // Error: B::foo does not override A::foo
                               // (signature mismatch)
    void foo() override; // OK: B::foo overrides A::foo
    void bar() override; // Error: A::bar is not virtual
};
```

## inline

## Inheritance
- Multiple inheritance:
```cpp
class CRectangle: public CPolygon, public COutput;
```
- Virtual Inheritance:
```cpp
class A;
class B : public virtual A;
class C : public virtual A;
// members of A will only have 1 copy
class D : public B, public C;
```
- Override: signature must match! basic class member function must be virtual!
```cpp
struct A {
  virtual void foo(); // must be virtual to be overriden
  void bar();
}
struct B : A {
  void foo() const override; // Error: B::foo does not override A::foo
                               // (signature mismatch)
  // OK: B::foo overrides A::foo
  // could also be virtual void foo() override;
  void foo() override; 
  void bar() override; // Error: A::bar is not virtual
};
```
- If a method in a base class will be redefined in a derived class, you should make it virtual.
- If the method should not be redefined, you should make it nonvirtual.

## Friend
```cpp
class B;
class A {
	friend rtype func(); // allow private members' access
	friend class B; // allow access to val
private:
	type val;
};
class B {
	void func(A a); // access to a.val allowed
};
```