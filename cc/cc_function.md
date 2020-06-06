# Functions

- How a function is called?
```cpp
int __stdcall function(int a,int b);
int __cdecl function(int a,int b);
```

## Function Pointer
```cpp
void HelloWorld(int a) {
	std::cout << "Hello World" << a << std::endl;
}
auto f = HelloWorld; // correct
void(*f)(int) = HelloWorld; // correct

typedef void(*func)(int); // correct
func f = HelloWorld;
f(3);
```
- std::function
```cpp
std::function<void(int)> f_display = print_num;
f_display(-9);
```

## Overloading:
```cpp
int operate(int a, int b);
float operate(float a, float b);
```

## inline: less overhead than regular call

## Polymorphism
- Overriding operators:
```cpp
Group& operator[](int id) {return group_[id];}
std::vector::operator =(const vector& x);
```
- Abstract Class
```cpp
class xxx {
	virtual void area() = 0;
};
```

## lambda function and std::function
- Lambda function:
```cpp
[](int x, int y) {return x + y;}
[](int& x) {++x;}
[]() {global_x++;}
[]{global_x++;}

[&](){} // all by reference
[=] // all by value
[x, &y] // x by value, y by referenc
[&, x]
[=, &z]

[&, value, this] // make every member under this available
```
- std::function
```cpp
template< class R, class... Args >
class function<R(Args...)>;

// example in Paddle:
// typedef std::function<BaseClass*(CreateArgs...)> ClassCreator;
// ClassCreator creator; return creator(args...);
// Return an instance of the given class
```
- lambda together with std::function<>()
```cpp
auto func = [&](int x) {...;}
void (*func_ptr)(int) = func;
func_ptr(4);

std::function<int()> func([](){xxxx; return 1;});

template<class R, class... Args>
class function<R(Args)>;
```