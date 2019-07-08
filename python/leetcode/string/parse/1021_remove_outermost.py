"""
1021. Remove Outermost Parentheses (Easy)

A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A 
and B are valid parentheses strings, and + represents string concatenation. 
For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist 
a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + 
P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the 
primitive decomposition of S.

Example 1:

Input: "(()())(())"
Output: "()()()"
Explanation:
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

Example 2:

Input: "(()())(())(()(()))"
Output: "()()()()(())"
Explanation:
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + 
"(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = 
"()()()()(())".

Example 3:

Input: "()()"
Output: ""
Explanation:
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".

Note:

S.length <= 10000
S[i] is "(" or ")"
S is a valid parentheses string
"""


class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        in_list = []
        cnt = 0
        st = 0

        if S == "":
            return S

        # analysis
        if S[0] == "(":
            cnt = 1
        else:
            cnt = -1
        cnt = 1
        n = len(S)
        for i in range(1, n):
            # make statistics
            if S[i] == "(":
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                # append
                in_list.append(S[st : i + 1])
                st = i + 1
        result = ""
        for item in in_list:
            result += item[1:-1]
        return result


if __name__ == "__main__":
    a = Solution()
    print(a.removeOuterParentheses("(()())(())"))
    print(a.removeOuterParentheses("(()())(())(()(()))"))
    print(a.removeOuterParentheses("()()"))
