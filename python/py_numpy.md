# Numpy Summary

## Array
- Creation:
```python
x = np.float32(1.0)
y = np.int_([1,2,4]) # int64
np.array([1, 2, 3], dtype='f')
np.array([ 1.,  2.,  3.], dtype=np.float32)

# complex numbers
x = np.array([[1,2.0],[0,0],(1+1j,3.)])

x = np.zeros([3,4])
x = np.ndarray([1,2,3])
x = np.ones([4,5])
```
- Reshape, range
```python
x = np.array(range(60))
y = x.reshape(3, 4, 5)
y[0]
y[0,:]
y[:1,:]

x = np.arange(15).reshape(3,5)
x.ndim
x.dtype
x.astype(np.float)

np.linspace(0, 2, 9)
```
- Manipulation
```python
a = np.identity(3)
a.ravel() # contiguous flattened array
a.flatten()
b = np.ones([3,3]) 
np.hstack([a,b]) # np.concatenate((a,b), axis=1)
np.vstack([a,b]) # np.concatenate((a,b), axis=0)
np.hsplit(a, 3)
np.vsplit(a, 3)
np.split(a, 3, axis=1)
```
- Array stat
```python
a = np.random.normal(size=[30, 10])
np.mean(a)
np.max(a)
np.min(a)
np.median(a)
```
- Array lookup:
```python
# a tuple with positions
pos = np.where(a>0)
for i,j in zip(pos[0], pos[1]):
  print(a[i,j])
```

## Linear Algorithm
- Linear solver:
```python
a = np.array([[1.,2.],[3.,4.]])
np.linalg.inv(a)

A = np.identity(3)
y = np.array([1., 2., 3.])
x = np.linalg.solve(A, y)
```

## Random generator
- Random generator
```python
a = np.random.normal(size=[30, 10])
```
- Random shuffle
```python
a = range(10)
np.random.shuffle(a)
```
- Set random seed
```python
np.random.seed(seed=123)
```