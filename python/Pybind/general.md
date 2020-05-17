# Pybind

## A Whole Summary
- http://pybind11.readthedocs.io/en/stable/basics.html

## Installation
- Make pybind11 folder in the same directory together with the codes:
```cmake
cmake_minimum_required(VERSION 2.8.12)
project(example)

add_subdirectory(pybind11)
pybind11_add_module(example example.cc)
```
- In *Linux*, if pybind is installed by apt-get, we can directly do
```cmake
find_package(pybind11)
```

## Binding
- Notice the same module name *example* should be the same as cmake
```cpp
#include <pybind11/pybind11.h>

int add(int i, int j) {
    return i + j;
}

PYBIND11_MODULE(example, m) {
    m.doc() = "pybind11 example plugin"; // optional module docstring

    m.def("add", &add, "A function which adds two numbers");
}
```
- Then when we call with no error
```python
import example
```
everything can work properly.
- The *PYBIND11_MODULE()* macro creates a function that will be called when an import statement is issued from within Python. 
- The module name *example* is given as the first macro argument (it should not be in quotes). 
- The second argument *m* defines a variable of type py::module which is the main interface for creating bindings. 
- The method *module::def()* generates binding code that exposes the add() function to Python.
- Key word:
```cpp
m.def("add", &add, "A function which adds two numbers",
      py::arg("i"), py::arg("j"));
```
- Default parameter:
```cpp
m.def("add", &add, "A function which adds two numbers",
      py::arg("i") = 1, py::arg("j") = 2);
```
- Exporting variables
```cpp
PYBIND11_MODULE(example, m) {
    m.attr("the_answer") = 42;
    py::object world = py::cast("World");
    m.attr("what") = world;
}
```

## Object Oriented
- Define in C++; binding with Python:
```cpp
struct Pet {
    Pet(const std::string &name) : name(name) { }
    void setName(const std::string &name_) { name = name_; }
    const std::string &getName() const { return name; }

    std::string name;
};

#include <pybind11/pybind11.h>
namespace py = pybind11;

PYBIND11_MODULE(example, m) {
    py::class_<Pet>(m, "Pet")
        .def(py::init<const std::string &>())
        .def("setName", &Pet::setName)
        .def("getName", &Pet::getName);
}
```
- Enable repr by lambda function:
```cpp
py::class_<Pet>(m, "Pet")
    .def(py::init<const std::string &>())
    .def("setName", &Pet::setName)
    .def("getName", &Pet::getName)
    .def("__repr__",
        [](const Pet &a) {
            return "<example.Pet named '" + a.name + "'>";
        }
    );
```
- Instance and static fields
```cpp
class Pet {
public:
    Pet(const std::string &name) : name(name) { }
    void setName(const std::string &name_) { name = name_; }
    const std::string &getName() const { return name; }
private:
    std::string name;
};

py::class_<Pet>(m, "Pet")
    .def(py::init<const std::string &>())
    .def_property("name", &Pet::getName, &Pet::setName)
    // ... remainder ...
```
- Dynamic attributes:
```python
class Pet:
  name = 'Molly'

p = Pet()
p.name = 'Charly'  # overwrite existing
p.age = 2  # dynamically add a new attribute
```
add py::dynamic_attr() in C++ to enable:
```cpp
py::class_<Pet>(m, "Pet", py::dynamic_attr())
    .def(py::init<>())
    .def_readwrite("name", &Pet::name);
```
- Inheritance