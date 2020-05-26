# STL Library

## Introduction
- Standard Template Library (stl). It provides four components called algorithms, containers, functions, and iterators.
- 13 headers
```cpp
<functional>
<iterator>
<vector><list><map><deque><queue><set><stack>
<memory>
<numeric>
<utility>
```

## Good articls
- http://www.cnblogs.com/CnZyy/p/3317999.html
- http://huqunxing.site/2016/09/29/C++STL%E8%AF%A6%E8%A7%A3%E4%B9%8B%E7%AE%97%E6%B3%95/

## Algorithm, Functional
- Sorting and ranking
```cpp
std::sort(a.begin(), a.end());
std::sort(a.begin(), a.begin()+4);

inplace_merge();
merge();
nth_element();
partial_sort();
partial_sort_copy();
partition();
random_shuffle();
reverse();
reverse_copy();
rotate();
rotate_copy();
stable_sort();
stable_partition();
```
- Generation
```cpp
std::fill();
std::iota(); // similar to fill?
std::fill_n();
std::for_each()
std::generate()
std::generate_n()
std::transform()
```
- Comparison, relation
```cpp
std::min();
std::max();
std::equal();

include();
lexicographical_compare();
max_element();
min_element();
mismatch();
```
- Modify
```cpp
#include <algorithm> // until c++11
#include <utility> // since c++11
void swap(T& a, T& b);

swap_range();
copy();
```
- Search:
```cpp
adjacent_find()
binary_search()
count()
count_if()
equal_range()
find()
find_end()
find_first_of()
find_if()
lower_bound()
upper_bound()
search()
search_n()
```
- Delete and Replacement
```cpp
copy //	复制序列
copy_backward//	与copy相同，不过元素是以相反顺序被拷贝。
iter_swap //	交换两个ForwardIterator的值。
remove //	删除指定范围内所有等于指定元素的元素。注意，该函数不是真正删除函数。内置函数不适合使用remove和remove_if函数。
remove_copy //	将所有不匹配元素复制到一个制定容器，返回OutputIterator指向被拷贝的末元素的下一个位置。
remove_if //	删除指定范围内输入操作结果为true的所有元素。
remove_copy_if //	将所有不匹配元素拷贝到一个指定容器。
replace //	将指定范围内所有等于vold的元素都用vnew代替。
replace_copy //	与replace类似，不过将结果写入另一个容器。
replace_if //	将指定范围内所有操作结果为true的元素用新值代替。
replace_copy_if//	与replace_if，不过将结果写入另一个容器。
unique //	清除序列中重复元素，和remove类似，它也不能真正删除元素。重载版本使用自定义比较操作。
unique_copy //	与unique类似，不过把结果输出到另一个容器。
```
- Combinatorial
```cpp
std::next_permutation()
std::prev_permutation()
```
- Set algorithms
```cpp
set_union();
set_intersection();
set_difference();
set_symmetric_difference();
```
- Heap manipulation
```cpp
make_heap()
pop_heap()
push_heap()
sort_heap()
```

## functional
- std::hash
```cpp
template< class Key >
struct hash;

template<> struct hash<bool>;
template<> struct hash<char>;
template<> struct hash<signed char>;
...
```

## Numeric Library
- Complex
```cpp
std::complex;
```
- Arithmetic
```cpp
accumulate();
partial_sum();
inner_product();
adjacent_difference();
```

## Utility Library
- Data stucture
```cpp
pair

tuple // tuple<double, char, std::string> a;
std::tie(); // to make a tuple
```
- Enable type if the condition is met. The type T is enabled as member type enable_if::type if Cond is true. Otherwise, enable_if::type is not defined.
```cpp
template< bool B, class T = void >
struct enable_if;

// example
template <typename Actor,
    std::enable_if_t<has_func_reward<Actor>::value>* U = nullptr>
float get_reward(const Actor& actor, const Node* node) {
    return actor.reward(*node->getStatePtr(), node->getValue());
}
```
- Initialization
```cpp
std::initializer_list<TF_Operation*>

 S<int> s = {1, 2, 3, 4, 5}; // copy list-initialization
```
- Type Support
```cpp
template< class T >
struct is_fundamental;

std::is_fundamental<int>::value; // true
std::is_fundamental<int&>::value; // false

std::is_trivially_constructible<T,Args&&...>::value
std::is_copy_assignable<T>::value;
```
- numeric limits
```cpp
template <class T>
class numeric_limits;

std::numeric_limits<size_t>::max();
```