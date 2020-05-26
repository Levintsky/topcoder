"""
856. Score of Parentheses (Medium)

Given a balanced parentheses string S, compute the score of the string based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.

Example 1:

Input: "()"
Output: 1
Example 2:

Input: "(())"
Output: 2
Example 3:

Input: "()()"
Output: 2
Example 4:

Input: "(()(()))"
Output: 6
 

Note:

S is a balanced parentheses string, containing only ( and ).
2 <= S.length <= 50
"""

class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        last_idx = -1
        slist = []
        cum = 0
        n = len(S)
        for i, c in enumerate(S):
            if S[i] == '(':
                cum += 1
            else:
                cum -= 1
            if cum == 0:
                slist.append(S[last_idx+1:i+1])
                last_idx = i
        # for each
        if len(slist) == 1:
            if slist[0] == '()':
                return 1
            else:
                return 2 * self.scoreOfParentheses(S[1:-1])
        else:
            return sum([self.scoreOfParentheses(item) for item in slist])



if __name__ == "__main__":
    a = Solution()
    print(a.scoreOfParentheses("()"))
    print(a.scoreOfParentheses("(())"))
    print(a.scoreOfParentheses("()()"))
    print(a.scoreOfParentheses("(()(()))"))
