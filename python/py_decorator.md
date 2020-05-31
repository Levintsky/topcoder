# Decorator

## A wrapper on a function:
- Some good materials: http://www.cnblogs.com/SeasonLee/articles/1719444.html, https://www.cnblogs.com/cicaday/p/python-decorator.html
- Function has arugements:
```python
def debug(func):
    def wrapper(*args, **kwargs):  # fit any arguments passing
        print "[DEBUG]: enter {}()".format(func.__name__)
        print 'Prepare and say...',
        return func(*args, **kwargs)
    return wrapper  # return

@debug
def say(something):
    print "hello {}!".format(something)
```
- Decorator with arguments:
```python
def logging(level):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print "[{level}]: enter function {func}()".format(
                level=level,
                func=func.__name__)
            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper

@logging(level='INFO')
def say(something):
    print "say {}!".format(something)

# equal to
# say = logging(level='INFO')(say)

@logging(level='DEBUG')
def do(something):
    print "do {}...".format(something)

if __name__ == '__main__':
    say('hello')
    do("my work")
```

## Built-in decorators: property
- property decorators, functions with property decorators returns a property object
```python
@property
def x(self):
  
@setter
@getter
@deleter
```
- Example in Minigo:
```python
class MCTSNode(object):
    @property
    def N(self):
        return self.parent.child_N[self.fmove]

    @N.setter
    def N(self, value):
        self.parent.child_N[self.fmove] = value

    @property
    def W(self):
        return self.parent.child_W[self.fmove]

    @W.setter
    def W(self, value):
        self.parent.child_W[self.fmove] = value
```
- Example in pytorch
```python
class Uniform(Distribution):
    @property
    def mean(self):
        return (self.high + self.low) / 2

    @property
    def stddev(self):
        return (self.high - self.low) / 12**0.5

    @property
    def variance(self):
        return (self.high - self.low).pow(2) / 12
```

## Built-in decorators: class/static method
- **classmethod** mainly used in constructor.
    - In python, the only construction function is new:
```python
__new__()
@classmethod
def fff(cls, n):
    return cls(...)
```
    - classmethod() to provide different initialization. Examples in pytorch:
```python
@classmethod
def from_pretrained(cls, embeddings):
    embeddings = cls(...)
    return embeddings
```
- **staticmethod** for functions belonging to class rather than instance:
```python
class BatchNorm(Function):
    @staticmethod
    def forward(self, ...):
        ...

    def backward(self, ...):
        ...
```

- Example
```python
class A(object):
    def m1(self, n):
        print("self:", self)

    @classmethod
    def m2(cls, n):
        print("cls:", cls)

    @staticmethod
    def m3(n):
        pass

a = A()
a.m1(1) # self: <__main__.A object at 0x000001E596E41A90>
A.m2(1) # cls: <class '__main__.A'>
A.m3(1)
```
- Used to access private members
```python
class Circle(object):
   __pi = 3.14

   def __init__(self, r):
       self.r = r

   def area(self):
       """
       """
       return self.r**2 * self.__pi

   def __girth(self):
       """
       """
       return 2*self.r * self.__pi

   @classmethod
   def pi(cls):
       return cls.__pi

print(Circle.pi())
circle1 = Circle(2)
# print(circle1.__girth())
```
