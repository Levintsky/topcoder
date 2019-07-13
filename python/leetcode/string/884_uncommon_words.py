"""
884. Uncommon Words from Two Sentences (Easy)

We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order.

 

Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]
 

Note:

0 <= A.length <= 200
0 <= B.length <= 200
A and B both contain only spaces and lowercase letters.
"""

class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        A_set = collections.Counter(A.split())
        B_set = collections.Counter(B.split())
        res = []
        for k in A_set:
            if A_set[k] == 1 and k not in B_set:
                res.append(k)
        for k in B_set:
            if B_set[k] == 1 and k not in A_set:
                res.append(k)
        return res