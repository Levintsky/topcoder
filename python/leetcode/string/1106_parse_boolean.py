"""
1106. Parsing A Boolean Expression (Hard)

Return the result of evaluating a given boolean expression, represented as a string.

An expression can either be:

"t", evaluating to True;
"f", evaluating to False;
"!(expr)", evaluating to the logical NOT of the inner expression expr;
"&(expr1,expr2,...)", evaluating to the logical AND of 2 or more inner expressions expr1, expr2, ...;
"|(expr1,expr2,...)", evaluating to the logical OR of 2 or more inner expressions expr1, expr2, ...
 

Example 1:

Input: expression = "!(f)"
Output: true
Example 2:

Input: expression = "|(f,t)"
Output: true
Example 3:

Input: expression = "&(t,f)"
Output: false
Example 4:

Input: expression = "|(&(t,f,t),!(t))"
Output: false
 

Constraints:

1 <= expression.length <= 20000
expression[i] consists of characters in {'(', ')', '&', '|', '!', 't', 'f', ','}.
expression is a valid expression representing a boolean, as given in the description.
"""

class Solution(object):
    def parseBoolExpr(self, expression):
        """
        :type expression: str
        :rtype: bool
        """
        # parse recursively
        if expression == "f" or expression == "(f)":
            return False
        elif expression == "t" or expression == "(t)":
            return True
        if expression[0] == "!": # not
            return not self.parseBoolExpr(expression[2:-1])
        elif expression[0] == "&":
            sub = expression[2:-1]
            sublist = self.subsplit(sub)
            for item in sublist:
                if not self.parseBoolExpr(item):
                    return False
            return True
        else: # |
            sub = expression[2:-1]
            sublist = self.subsplit(sub)
            for item in sublist:
                if self.parseBoolExpr(item):
                    return True
            return False

    def subsplit(self, sub):
        sublist = sub.split(",")
        tmp = sublist[0]
        cnt = sublist[0].count("(") - sublist[0].count(")")
        flist = []
        if cnt == 0:
            flist.append(tmp)
            tmp = ""
        for item in sublist[1:]:
            if tmp != "":
                tmp += "," + item
            else:
                tmp = item
            cnt += item.count("(") - item.count(")")
            if cnt == 0:
                flist.append(tmp)
                tmp = ""
        return flist


if __name__ == "__main__":
    a = Solution()
    # print(a.parseBoolExpr("!(f)"))
    # print(a.parseBoolExpr("|(f,t)"))
    # print(a.parseBoolExpr("&(t,f)"))
    print(a.parseBoolExpr("|(&(t,f,t),!(t))"))