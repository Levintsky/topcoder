"""
641. Design Circular Deque (Medium)

Design your implementation of the circular double-ended queue (deque).

Your implementation should support following operations:

MyCircularDeque(k): Constructor, set the size of the deque to be k.
insertFront(): Adds an item at the front of Deque. Return true if the operation is successful.
insertLast(): Adds an item at the rear of Deque. Return true if the operation is successful.
deleteFront(): Deletes an item from the front of Deque. Return true if the operation is successful.
deleteLast(): Deletes an item from the rear of Deque. Return true if the operation is successful.
getFront(): Gets the front item from the Deque. If the deque is empty, return -1.
getRear(): Gets the last item from Deque. If the deque is empty, return -1.
isEmpty(): Checks whether Deque is empty or not. 
isFull(): Checks whether Deque is full or not.

Example:

MyCircularDeque circularDeque = new MycircularDeque(3); // set the size to be 3
circularDeque.insertLast(1);			// return true
circularDeque.insertLast(2);			// return true
circularDeque.insertFront(3);			// return true
circularDeque.insertFront(4);			// return false, the queue is full
circularDeque.getRear();  			// return 2
circularDeque.isFull();				// return true
circularDeque.deleteLast();			// return true
circularDeque.insertFront(4);			// return true
circularDeque.getFront();			// return 4

Note:

All values will be in the range of [0, 1000].
The number of operations will be in the range of [1, 1000].
Please do not use the built-in Deque library.
"""

class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.k = k
        self.data = [None] * k
        self.front = -1
        self.tail = -1
        self.size = 0

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.size == self.k:
            return False
        if self.size == 0:
            self.front = 0
            self.tail = 0
            self.data[0] = value
            self.size = 1
            return True
        self.front = (self.front - 1) % self.k
        self.data[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.size == self.k:
            return False
        if self.size == 0:
            self.front = 0
            self.tail = 0
            self.data[0] = value
            self.size = 1
            return True
        self.tail = (self.tail + 1) % self.k
        self.data[self.tail] = value
        self.size += 1
        return True

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.size == 0:
            return False
        self.front = (self.front + 1) % self.k
        self.size -= 1
        return True 

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.size == 0:
            return False
        self.tail = (self.tail - 1) % self.k
        self.size -= 1
        return True

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.size == 0:
            return -1
        else:
            return self.data[self.front]

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.size == 0:
            return -1
        else:
            return self.data[self.tail]

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.size == 0

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self.size == self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()


if __name__ == "__main__":
    obj = MyCircularDeque(3)
    print(obj.insertLast(1))
    print(obj.insertLast(2))
    print(obj.insertFront(3))
    print(obj.insertFront(4))
    print(obj.getRear())
    print(obj.isFull())
    print(obj.deleteLast())
    print(obj.insertFront(4))
    print(obj.getFront())
