"""
756. Pyramid Transition Matrix (Medium)

We are stacking blocks to form a pyramid. Each block has a color which is a one letter string.

We are allowed to place any color block C on top of two adjacent blocks of colors A and B, if and only if ABC is an allowed triple.

We start with a bottom row of bottom, represented as a single string. We also start with a list of allowed triples allowed. Each allowed triple is represented as a string of length 3.

Return true if we can build the pyramid all the way to the top, otherwise false.

Example 1:

Input: bottom = "BCD", allowed = ["BCG", "CDE", "GEA", "FFF"]
Output: true
Explanation:
We can stack the pyramid like this:
    A
   / \
  G   E
 / \ / \
B   C   D

We are allowed to place G on top of B and C because BCG is an allowed triple.  Similarly, we can place E on top of C and D, then A on top of G and E.
 

Example 2:

Input: bottom = "AABA", allowed = ["AAA", "AAB", "ABA", "ABB", "BAC"]
Output: false
Explanation:
We can't stack the pyramid to the top.
Note that there could be allowed triples (A, B, C) and (A, B, D) with C != D.

Note:

bottom will be a string with length in range [2, 8].
allowed will have length in range [0, 200].
Letters in all strings will be chosen from the set {'A', 'B', 'C', 'D', 'E', 'F', 'G'}.
"""

class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        self.memo = {}
        for item in allowed:
            if item[:2] not in self.memo:
                self.memo[item[:2]] = []
            self.memo[item[:2]].append(item[-1])
        res = self.helper(bottom)
        return res
            
    def helper(self, s):
        if len(s) <= 1:
            return True
        res = [""]
        n = len(s)
        for i in range(n-1):
            new_res = []
            if s[i:i+2] not in self.memo:
                return False
            for item in res:
                for new in self.memo[s[i:i+2]]:
                    new_res.append(item + new)
            res = new_res
        for item in res:
            if self.helper(item):
                return True
        return False
