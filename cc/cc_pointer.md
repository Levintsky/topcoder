# Smart pointer

- added benefit over using raw pointers is automatic memory management of dynamically allocated resources, so that you don't have to make explicit calls to delete.

## Pointer versus Reference
- https://blog.csdn.net/tianxiaolu1175/article/details/46889523
- reference
```cpp
int real = 2;
int& ref = real;

std::vector<int> vec;
vec.push_back(real);
vec.push_back(ref); // will change together
```
