"""
633. Sum of Square Numbers (Easy)

Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:
Input: 3
Output: False
"""

import math


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c == 0:
            return True
        a = 0
        while a * a * 2 <= c:
            b = round(math.sqrt(c - a ** 2))
            if b * b + a * a == c:
                return True
            a += 1
        return False
