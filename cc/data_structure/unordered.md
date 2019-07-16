# Unordered Nonlinear DS

## Hash Type
- unordered_map
```cpp
// example
#include <unordered_map>
unordered_map<int, char> map;

template<
    class Key,
    class T,
    class Hash = std::hash<Key>,
    class KeyEqual = std::equal_to<Key>,
    class Allocator = std::allocator< std::pair<const Key, T> >
> class unordered_map;

/* Element access */
mapped_type& operator[] ( const key_type& k );
mapped_type& operator[] ( key_type&& k );
mapped_type& at ( const key_type& k );
const mapped_type& at ( const key_type& k ) const;

/* Element lookup */
// auto item = map.find(key);
// item.first, item.second for key, value
iterator find ( const key_type& k );
const_iterator find ( const key_type& k ) const;
// 1 if existing, 0 otherwise
size_type count ( const key_type& k ) const;

/* Modifiers */
// generally, emplace(T1&&, T2&&)
template <class... Args>
pair<iterator, bool> emplace ( Args&&... args );
// insert(std::make_pair<T1, T2>(val1, val2));
pair<iterator,bool> insert ( const value_type& val );
// erase by key, iterator or range
erase();
```
- unordered_set