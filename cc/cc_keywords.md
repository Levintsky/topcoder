# All Keywords

- A good summary: https://blog.csdn.net/fyl_csdn/article/details/44905211, https://blog.csdn.net/scmuzi18/article/details/53696778
- 63 classic keywords in c++98/03.
```cpp
asm, auto, bool, break, case, catch, char, class, const, const_cast, continue, default, delete, do, double, dynamic_cast, else, enum, explicit, export, extern, false, float, for, friend, goto, if, inline, int, long, mutable, namespace, new, operator, private, protected, public, register, reinterpret_cast, return, short, signed, sizeof, static, static_cast, struct, switch, template, this, throw, true, try, typedef, typeid, typename, union, unsigned, using, virtual, void, volatile, wchar_t, while 
```
- New keywords in C++11
```cpp
alignas, alignof, char16_t, char32_t, constexpr, decltype, noexcept, nullptr, static_assert, thread_local, auto
```

## auto
To automatically infer variable type
```cpp
```

## boolean
```cpp
bool, true, false
```

## cast
```cpp
const_cast; dynamic_cast; reinterpret_cast; static_cast;
```

## char
```cpp
char; wchar_t
```

## class related
```cpp
explicit
friend
```
- override (since c++11)

## control flow
```cpp
break; cotinue; goto;
```
- switch
```cpp
switch; case; default;
```

## execution
```cpp
asm
```
- volatile: tell compiler not to optimize this part (https://www.cnblogs.com/yc_sunniwell/archive/2010/07/14/1777432.html)
```cpp
int i = 10;
int a = i;
// always 10
printf("i = %d", a);

// change i without telling compiler
__asm {
 mov dword ptr [ebp-4], 20h
}
int b = i;
// compiler optimize
// debug mode: 32, release mode: 10
printf("i = %d", b);
```
- constexpr
```
- mutable: always mutable, override const
```cpp
struct test {
  int a;
  mutable int b;
};
const test a;
a.a = 11; // error
a.b = 22; // OK
```

## exception
```cpp
catch; throw; try;
```

## extern
- some good links: https://www.cnblogs.com/yc_sunniwell/archive/2010/07/14/1777431.html
```cpp
// use C in C++ to avoid problems in compiling
extern "C" {}
```

## operator
```cpp
new, delete
```

## static
- static: static objects will be on heap rather than stack;
- Case 1: global static
```cpp
static int Temp = 10;  
void Test();  
int main() {}  
```
- Case 2: local static, can't be called outside function, but will remain in the memory after execution
```cpp
// main function
for(int i=0; i<5; i++)  
  Test(); // will be 10, 11, 12, ...  

// Test function define
void Test() {
  static int Temp = 10;
  std::cout << Temp << std::endl;
  Temp++;
}
```
- Case 3: static function (only visible in this function; if used somewhere else, *extern* required)
```cpp
static void Test();
```
- Case 4: static in class
```cpp
class test {
  // shared across instances
  static int T;
  // static member function
  static show(); {std::cout << T;}
};

// initialization only allowed outside
int test::T = 0;

test instance;
instance.show(); // correct
test::show(); // also correct
```

## type
```cpp
struct, class, union
typedef
```