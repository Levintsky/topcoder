"""
1172. Dinner Plate Stacks (Hard)

You have an infinite number of stacks arranged in a row and numbered (left to right) from 0, each of the stacks has the same maximum capacity.

Implement the DinnerPlates class:

DinnerPlates(int capacity) Initializes the object with the maximum capacity of the stacks.
void push(int val) pushes the given positive integer val into the leftmost stack with size less than capacity.
int pop() returns the value at the top of the rightmost non-empty stack and removes it from that stack, and returns -1 if all stacks are empty.
int popAtStack(int index) returns the value at the top of the stack with the given index and removes it from that stack, and returns -1 if the stack with that given index is empty.
Example:

Input: 
["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"]
[[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]
Output: 
[null,null,null,null,null,null,2,null,null,20,21,5,4,3,1,-1]

Explanation: 
DinnerPlates D = DinnerPlates(2);  // Initialize with capacity = 2
D.push(1);
D.push(2);
D.push(3);
D.push(4);
D.push(5);         // The stacks are now:  2  4
                                           1  3  5
                                           ﹈ ﹈ ﹈
D.popAtStack(0);   // Returns 2.  The stacks are now:     4
                                                       1  3  5
                                                       ﹈ ﹈ ﹈
D.push(20);        // The stacks are now: 20  4
                                           1  3  5
                                           ﹈ ﹈ ﹈
D.push(21);        // The stacks are now: 20  4 21
                                           1  3  5
                                           ﹈ ﹈ ﹈
D.popAtStack(0);   // Returns 20.  The stacks are now:     4 21
                                                        1  3  5
                                                        ﹈ ﹈ ﹈
D.popAtStack(2);   // Returns 21.  The stacks are now:     4
                                                        1  3  5
                                                        ﹈ ﹈ ﹈ 
D.pop()            // Returns 5.  The stacks are now:      4
                                                        1  3 
                                                        ﹈ ﹈  
D.pop()            // Returns 4.  The stacks are now:   1  3 
                                                        ﹈ ﹈   
D.pop()            // Returns 3.  The stacks are now:   1 
                                                        ﹈   
D.pop()            // Returns 1.  There are no stacks.
D.pop()            // Returns -1.  There are still no stacks.

Constraints:

1 <= capacity <= 20000
1 <= val <= 20000
0 <= index <= 100000
At most 200000 calls will be made to push, pop, and popAtStack.
"""

import bisect


class DinnerPlates(object):
    # TLE!

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.stacks = [[]]
        self.capacity = capacity
        self.active_list = [0]
        self.pop_list = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        # append val in the leftmost stacks (active-list)
        # update active-list (remove if full)
        # update pop-list (add if the first one)
        idx = self.active_list[0]
        self.stacks[idx].append(val)
        if idx not in self.pop_list:
            bisect.insort(self.pop_list, idx)
        if len(self.stacks[idx]) == self.capacity:
            self.active_list = self.active_list[1:]
            if len(self.active_list) == 0:
                self.stacks.append([])
                self.active_list.append(len(self.stacks)-1)

    def pop(self):
        """
        :rtype: int
        """
        if len(self.pop_list) == 0:
            return -1
        idx = self.pop_list[-1]
        res = self.stacks[idx].pop() # pop-right
        if idx not in self.active_list:
            bisect.insort(self.active_list, idx)
        if len(self.stacks[idx]) == 0:
            self.pop_list.pop()
        return res

    def popAtStack(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index >= len(self.stacks) or len(self.stacks[index]) == 0:
            return -1
        res = self.stacks[index].pop()
        if len(self.stacks[index]) == self.capacity - 1:
            bisect.insort(self.active_list, index)
        if len(self.stacks[index]) == 0:
            self.pop_list.remove(index)
        return res


if __name__ == "__main__":
    a = DinnerPlates(2)
    for i in range(1, 6):
        a.push(i)
    print(a.popAtStack(0))
    a.push(20)
    a.push(21)
    print(a.popAtStack(0))
    print(a.popAtStack(2))
    for i in range(5):
        print(a.pop())
# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)

"""
Solution 1
Use a list stacks to save all stacks.
Use a heap queue q to find the leftmost available stack.

push, O(logN) time
pop, amortized O(1) time
popAtStack, O(logN) time

class DinnerPlates(object):
    def __init__(self, capacity):
        self.c = capacity
        self.q = []
        self.stacks = []

    def push(self, val):
        while self.q and self.q[0] < len(self.stacks) and len(self.stacks[self.q[0]]) == self.c:
            heapq.heappop(self.q)
        if not self.q:
            heapq.heappush(self.q, len(self.stacks))
            self.stacks.append([])
        self.stacks[self.q[0]].append(val)

    def pop(self):
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index):
        if 0 <= index < len(self.stacks) and self.stacks[index]:
            heapq.heappush(self.q, index)
            return self.stacks[index].pop()
        return -1
"""
