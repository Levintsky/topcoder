"""
710. Random Pick with Blacklist (Hard)

Given a blacklist B containing unique integers from [0, N), write a function to return a uniform random integer from [0, N) which is NOT in B.

Optimize it such that it minimizes the call to system’s Math.random().

Note:

1 <= N <= 1000000000
0 <= B.length < min(100000, N)
[0, N) does NOT include N. See interval notation.
Example 1:

Input: 
["Solution","pick","pick","pick"]
[[1,[]],[],[],[]]
Output: [null,0,0,0]
Example 2:

Input: 
["Solution","pick","pick","pick"]
[[2,[]],[],[],[]]
Output: [null,1,1,1]
Example 3:

Input: 
["Solution","pick","pick","pick"]
[[3,[1]],[],[],[]]
Output: [null,0,0,2]
Example 4:

Input: 
["Solution","pick","pick","pick"]
[[4,[2]],[],[],[]]
Output: [null,1,3,1]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has two arguments, N and the blacklist B. pick has no arguments. Arguments are always wrapped with a list, even if there aren't any.
"""

import random


class Solution(object):
    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        # self.N = N
        # self.blacklist = set(blacklist)
        self.memo = {}
        for item in blacklist:
            self.memo[item] = -1
        self.M = N - len(self.memo)
        for b in blacklist:
            if b < self.M:
                while N - 1 in self.memo:
                    N -= 1
                self.memo[b] = N - 1
                N -= 1

    def pick(self):
        """
        :rtype: int
        """
        """
        while True:
            k = random.randint(0, self.N-1)
            if k not in self.blacklist:
                return k
        """
        p = random.randint(0, self.M - 1)
        if p in self.memo:
            return self.memo[p]
        return p


if __name__ == "__main__":
    a = Solution(10, [3, 5, 8, 9])
    for i in range(20):
        print(a.pick())
# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()
