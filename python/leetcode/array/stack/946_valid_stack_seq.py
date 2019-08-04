"""
946. Validate Stack Sequences (Medium)

Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.

Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.

Note:

0 <= pushed.length == popped.length <= 1000
0 <= pushed[i], popped[i] < 1000
pushed is a permutation of popped.
pushed and popped have distinct values.
"""

class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        s = []
        i1, i2 = 0, 0
        while i1 < len(pushed) or i2 < len(popped):
            if s and s[-1] == popped[i2]:
                s.pop()
                i2 += 1
            elif i1 == len(pushed):
                return False
            elif pushed[i1] == popped[i2]:
                i1 += 1
                i2 += 1
            else:
                s.append(pushed[i1])
                i1 += 1
        return True
        
