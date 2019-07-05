"""
528. Random Pick with Weight (Medium)

Given an array w of positive integers, where w[i] describes the weight of index 
i, write a function pickIndex which randomly picks an index in proportion to 
its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
Example 1:

Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
Example 2:

Input: 
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. 
Solution's constructor has one argument, the array w. pickIndex has 
no arguments. Arguments are always wrapped with a list, even if 
there aren't any.
"""

import bisect, random


class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.data = [0]
        for w_ in w:
        	self.data.append(self.data[-1] + w_)
        self.data = self.data[1:]

    def pickIndex(self):
        """
        :rtype: int
        """
        rand = random.randint(1, self.data[-1])
        idx = bisect.bisect_left(self.data, rand)
        return idx


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


if __name__ == "__main__":
    a = Solution([1, 3])
    for _ in range(10):
        print(a.pickIndex())