"""
1096. Brace Expansion II (Hard)

Under a grammar given below, strings can represent a set of lowercase words.  Let's use R(expr) to denote the set of words the expression represents.

Grammar can best be understood through simple examples:

Single letters represent a singleton set containing that word.
R("a") = {"a"}
R("w") = {"w"}
When we take a comma delimited list of 2 or more expressions, we take the union of possibilities.
R("{a,b,c}") = {"a","b","c"}
R("{{a,b},{b,c}}") = {"a","b","c"} (notice the final set only contains each word at most once)
When we concatenate two expressions, we take the set of possible concatenations between two words where the first word comes from the first expression and the second word comes from the second expression.
R("{a,b}{c,d}") = {"ac","ad","bc","bd"}
R("{a{b,c}}{{d,e},f{g,h}}") = R("{ab,ac}{dfg,dfh,efg,efh}") = {"abdfg", "abdfh", "abefg", "abefh", "acdfg", "acdfh", "acefg", "acefh"}
Formally, the 3 rules for our grammar:

For every lowercase letter x, we have R(x) = {x}
For expressions e_1, e_2, ... , e_k with k >= 2, we have R({e_1,e_2,...}) = R(e_1) ∪ R(e_2) ∪ ...
For expressions e_1 and e_2, we have R(e_1 + e_2) = {a + b for (a, b) in R(e_1) × R(e_2)}, where + denotes concatenation, and × denotes the cartesian product.
Given an expression representing a set of words under the given grammar, return the sorted list of words that the expression represents.

 

Example 1:

Input: "{a,b}{c{d,e}}"
Output: ["acd","ace","bcd","bce"]
Example 2:

Input: "{{a,z},a{b,c},{ab,z}}"
Output: ["a","ab","ac","z"]
Explanation: Each distinct word is written only once in the final answer.

Constraints:

1 <= expression.length <= 50
expression[i] consists of '{', '}', ','or lowercase English letters.
The given expression represents a set of words based on the grammar given in the description.
"""

"""
Solution 1: two functions (split and concatenate calls each other)

Solution 2:
The general idea
Split expressions into groups separated by top level ','; for each top-level sub expression (substrings with braces), process it and add it to the corresponding group; finally combine the groups and sort.

Thought process
in each call of the function, try to remove one level of braces
maintain a list of groups separated by top level ','
when meets ',': create a new empty group as the current group
when meets '{': check whether current level is 0, if so, record the starting index of the sub expression;
always increase level by 1, no matter whether current level is 0
when meets '}': decrease level by 1; then check whether current level is 0, if so, recursively call braceExpansionII to get the set of words from expresion[start: end], where end is the current index (exclusive).
add the expanded word set to the current group
when meets a letter: check whether the current level is 0, if so, add [letter] to the current group
base case: when there is no brace in the expression.
finally, after processing all sub expressions and collect all groups (seperated by ','), we initialize an empty word_set, and then iterate through all groups
for each group, find the product of the elements inside this group
compute the union of all groups
sort and return
note that itertools.product(*group) returns an iterator of tuples of characters, so we use''.join() to convert them to strings
"""


class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """
        # first split
        def split(exp):
            print(exp)
            expl = []
            tmp = ""
            cnt = 0
            n = len(exp)
            for i in range(n):
                c = exp[i]
                if c == "{":
                    tmp += c
                    cnt += 1
                elif c == "}":  # or i == n-1:
                    tmp += c
                    cnt -= 1
                    if cnt == 0 and (i == n - 1 or exp[i + 1] != ","):
                        if tmp[0] == "{":
                            tmp = tmp[1:-1]
                        expl.append(tmp)
                        tmp = ""
                else:
                    tmp += c
                    if i == n - 1 or (cnt == 0 and exp[i + 1] == "{"):
                        expl.append(tmp)
                        tmp = ""
            return expl

        # expl = split(expression)
        # print(expl)

        def split2(exp):
            # split by ","
            expl = exp.split(",")
            n = len(expl)
            result = []
            cnt = 0
            tmp = ""
            for i in range(n):
                if tmp != "":
                    tmp += ","
                tmp += expl[i]
                cnt = tmp.count("{") - tmp.count("}")
                if cnt == 0:
                    # if tmp[0] == "{":
                    #     tmp = tmp[1:-1]
                    result.append(tmp)
                    tmp = ""
            return result

        # step 2: for each split, generate most
        def generate(exp):
            if "{" not in exp:
                tmpl = exp.split(",")
                return tmpl
            else:
                expl = split(exp)
                result = []
                for subexp in expl:
                    subres = generate2(subexp)
                    result.append(subres)
                full_result = result[0]
                for i in range(1, len(result)):
                    full_result = [
                        item1 + item2 for item1 in full_result for item2 in result[i]
                    ]
                    full_result = list(set(full_result))
                return full_result

        def generate2(exp):
            expl = split2(exp)
            result = set()
            for item in expl:
                subres = generate(item)
                for item in subres:
                    result.add(item)
            result = list(result)
            return result

        result = generate(expression)
        result.sort()
        return result

    def solve2(self, expression: str) -> List[str]:
        groups = [[]]
        level = 0
        for i, c in enumerate(expression):
            if c == "{":
                if level == 0:
                    start = i + 1
                level += 1
            elif c == "}":
                level -= 1
                if level == 0:
                    groups[-1].append(self.braceExpansionII(expression[start:i]))
            elif c == "," and level == 0:
                groups.append([])
            elif level == 0:
                groups[-1].append([c])
        word_set = set()
        for group in groups:
            word_set |= set(map("".join, itertools.product(*group)))
        return sorted(word_set)


if __name__ == "__main__":
    a = Solution()
    # print(a.braceExpansionII("{a,b}{c{d,e}}"))
    # print(a.braceExpansionII("{{a,z},a{b,c},{ab,z}}"))
    print(a.braceExpansionII("{{{c,g},{h,j},l},{a,{x,ia,o},w},{x,ia,o}}"))
