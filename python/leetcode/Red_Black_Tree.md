# Red-Black Tree

## Classical Cases
- Insert, remove, edit: all O(logn)
- LC-128: Longest consecutive sequence
- LC-315: Count of Smaller Numbers After Self
- LC-352: Data Stream as Disjoint Intervals
- LC-460: LFU Cache
- LC-480: Sliding Window median;

## Java
- TreeMap
	```java
	tree = new TreeMap<>();
	tree.put(val, new Interval(val, val)); // add
	tree.remove(v); // remove
	tree.containKey(val) // Query O(log(n))
	tree.remove(h); // Delete O(log(n))
	Integer l = tree.lowerKey(val); // Query lower-key O(log(n))
	Integer l = tree.higherKey(val); // Query higher-key O(log(n))
	```
- TreeSet
- HashMap

## C++: multiset
```cpp
multiset<int> window(nums.begin(), nums.begin()+k);
```
- **Multiple elements can have the same values**
- Query kth smallest;
```cpp
auto mid = next(window.begin(), k / 2);
```
- Insert:
```cpp
window.insert(nums[i]);
```
- Erase:
```cpp
window.erase(item);
```
- Lower bound (first <= item):
```cpp
window.lower_bound(item);
```

## Python: bisect
- Problem 480: Sliding Window median;