# User-Defined Types (Chap 2 of a Tour of C++)

## Overall
- Introduction
- Structures
- Classes
- Unions
- Enumerations
- Advice

## Structure and Unions
- Struct
```cpp
struct xxx {
	...
};
```
- A union is a struct in which all members are allocated at the same address
```cpp
union Value {
     Node* p;
     int i;
};
```

## Enumerate
```cpp
enum class Color { red, blue, green };
enum class Traffic_light { green, yellow, red };

Color col = Color::red;
Traffic_light light = Traffic_light::red;
```
- class after enum means strongly typed:
```cpp
Color x = red;                  // error: which red?
Color y = Traffic_light::red;   // error: that red is not a Color
int i = Color::red;        // error: Color::red is not an int
Color c = 2;               // initialization error: 2 is not a Color

Color z = Color::red;           // OK
Color x = Color{5};  // OK, but verbose
Color y {6};         // also OK
```