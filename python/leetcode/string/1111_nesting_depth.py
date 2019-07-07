"""
1111. Maximum Nesting Depth of Two Valid Parentheses Strings (Medium)

A string is a valid parentheses string (denoted VPS) if and only if it consists of 
"(" and ")" characters only, and:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are VPS's, or
It can be written as (A), where A is a VPS.
We can similarly define the nesting depth depth(S) of any VPS S as follows:

depth("") = 0
depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's
depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
For example,  "", "()()", and "()(()())" are VPS's (with nesting depths 0, 
1, and 2), and ")(" and "(()" are not VPS's. 

Given a VPS seq, split it into two disjoint subsequences A and B, such that A 
and B are VPS's (and A.length + B.length = seq.length).

Now choose any such A and B such that max(depth(A), depth(B)) is the 
minimum possible value.

Return an answer array (of length seq.length) that encodes such a choice of 
A and B:  answer[i] = 0 if seq[i] is part of A, else answer[i] = 1.  Note 
that even though multiple answers may exist, you may return any of them. 

Example 1:

Input: seq = "(()())"
Output: [0,1,1,1,1,0]
Example 2:

Input: seq = "()(())()"
Output: [0,0,0,1,1,0,1,1]

Constraints:

1 <= seq.size <= 10000
"""

class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        n = len(seq)
        if n == 0: return []
        self.result = [-1] * n
        self.parse(seq, 0, 0, n-1)
        max_h = max(self.result) + 1
        thr = (max_h - 1) // 2
        for i in range(n):
            if self.result[i] <= thr:
                self.result[i] = 0
            else:
                self.result[i] = 1
        return self.result

    def parse(self, seq, depth, i, j):
        if i >= j: return
        # go through and split
        slist = []
        st = i
        cnt = 0
        for ii in range(i, j+1):
            if seq[ii] == ")":
                cnt -= 1
            else:
                cnt += 1
            if cnt == 0:
                slist.append([st, ii])
                st = ii+1
        # case 1:
        if len(slist) == 1:
            self.result[i] = depth
            self.result[j] = depth
            self.parse(seq, depth+1, i+1, j-1)
        else:
            for st, end in slist:
                self.parse(seq, depth, st, end)

    def solve2(self, seq):
        n = len(seq)
        res = [0] * n
        cnt = 0
        for i, c in enumerate(seq):
            if i == 0:
                res[i] = cnt
                if c == "(":
                    cnt += 1
                else:
                    cnt -= 1
            else:
                if c == "(":
                    res[i] = cnt
                    cnt += 1
                else:
                    cnt -= 1
                    res[i] = cnt
        thr = (max(res) - 1) // 2
        for i in range(n):
            if res[i] <= thr:
                res[i] = 0
            else:
                res[i] = 1
        return res

if __name__ == "__main__":
    a = Solution()
    # print(a.maxDepthAfterSplit("(()())"))
    # rint(a.maxDepthAfterSplit("()(((())))()"))  
    print(a.solve2("(()())"))
    print(a.solve2("()(())()"))  
