"""
22. Generate Parentheses (Medium)

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        if n == 1:
            return ["()"]
        self.result = []

        def traverse(prefix, i, j):
            if i == 0 and j == 0:
                self.result.append(prefix)
                return
            if i == 0:
                prefix += ")" * j
                self.result.append(prefix)
                return
            if i == j:
                prefix += "("
                traverse(prefix, i - 1, j)
                return
            traverse(prefix + "(", i - 1, j)
            traverse(prefix + ")", i, j - 1)

        traverse("", n, n)
        return self.result


if __name__ == "__main__":
    a = Solution()
    print(a.generateParenthesis(3))
