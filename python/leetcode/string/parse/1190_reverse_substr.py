"""
1190. Reverse Substrings Between Each Pair of Parentheses (Medium)

Given a string s that consists of lower case English letters and brackets. 

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any bracket.

Example 1:

Input: s = "(abcd)"
Output: "dcba"
Example 2:

Input: s = "(u(love)i)"
Output: "iloveu"
Example 3:

Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Example 4:

Input: s = "a(bcdefghijkl(mno)p)q"
Output: "apmnolkjihgfedcbq"
 

Constraints:

0 <= s.length <= 2000
s only contains lower case English characters and parentheses.
It's guaranteed that all parentheses are balanced.
"""

class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        # recursively
        # edge case 1:
        # print('working on:', s)
        if s == "" or '(' not in s:
            return s
        """
        if s[0] == '(':
            res = self.reverseParentheses(s[1:-1])
            return res[::-1]
        """
        stack = []
        cnt, curr = 0, ""
        for c in s:
            if c == "(":
                cnt += 1
            elif c == ")":
                cnt -= 1

            curr += c
            if cnt == 0:
                stack.append(curr)
                curr = ""
        # edge case 2:
        if len(stack) == 1:
            # "(xxxx)"
            res = self.reverseParentheses(stack[0][1:-1])
            return res[::-1]

        result_list = []
        for item in stack:
            result_list.append(self.reverseParentheses(item))
        return "".join(result_list)


if __name__ == "__main__":
    a = Solution()
    print(a.reverseParentheses("(abcd)"))
    print(a.reverseParentheses("(u(love)i)"))
    print(a.reverseParentheses("(ed(et(oc))el)"))
    print(a.reverseParentheses("a(bcdefghijkl(mno)p)q"))
    print(a.reverseParentheses("wnb(((z()qw)eyt)(bx(()ye)))"))
