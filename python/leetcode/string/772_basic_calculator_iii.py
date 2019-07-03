"""
772. Basic Calculator III (Hard)

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

The expression string contains only non-negative integers, +, -, *, / operators , open ( and closing parentheses ) and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-2147483648, 2147483647].

Some examples:

"1 + 1" = 2
" 6-4 / 2 " = 4
"2*(5+5*2)/3+(6/2+8)" = 21
"(2+6* 3+5- (3*14/7+2)*5)+3"=-12
 

Note: Do not use the eval built-in library function.
"""

def isDigit(c):
    return ord(c) >= ord('0') and ord(c) <= ord('9')

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        l1, o1 = 0, 1
        l2, o2 = 1, 1
        i = 0
        while i < len(s):
            c = s[i]
            if isDigit(c):
                num = ord(c) - ord('0')
                while i + 1 < len(s) and isDigit(s[i+1]):
                    i += 1
                    num = num * 10 + ord(s[i]) - ord('0')
                l2 = l2 * num if o2 == 1 else l2 // num
            elif c == "(":
                j = i # back up
                cnt = 0
                while i < len(s):
                    if s[i] == "(":
                        cnt += 1
                    elif s[i] == ")":
                        cnt -= 1
                    if cnt == 0:
                        break
                    i += 1
                num = self.calculate(s[j+1:i])
                l2 = l2 * num if o2 == 1 else l2 // num
            elif c in ["*", "/"]:
                o2 = 1 if c == "*" else -1
            elif c in ["+", "-"]:
                if i != 0:
                    l1 = l1 + o1 * l2
                o1 = 1 if c == "+" else -1
                l2, o2 = 1, 1

            i += 1
        return l1 + o1 * l2


if __name__ == "__main__":
    a = Solution()
    print(a.calculate("2*(5+5*2)/3+(6/2+8)"))
    print(a.calculate("(2+6* 3+5- (3*14/7+2)*5)+3"))
    print(a.calculate("3*14/7"))
    print(a.calculate("-1+4*3/3/3"))
