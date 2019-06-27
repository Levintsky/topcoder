"""
1023. Camelcase Matching (Medium)

A query word matches a given pattern if we can insert lowercase letters to the pattern word so that it equals the query. (We may insert each character at any position, and may insert 0 characters.)

Given a list of queries, and a pattern, return an answer list of booleans, where answer[i] is true if and only if queries[i] matches the pattern.



Example 1:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
Output: [true,false,true,true,false]
Explanation:
"FooBar" can be generated like this "F" + "oo" + "B" + "ar".
"FootBall" can be generated like this "F" + "oot" + "B" + "all".
"FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".
Example 2:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
Output: [true,false,true,false,false]
Explanation:
"FooBar" can be generated like this "Fo" + "o" + "Ba" + "r".
"FootBall" can be generated like this "Fo" + "ot" + "Ba" + "ll".
Example 3:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"
Output: [false,true,false,false,false]
Explanation:
"FooBarTest" can be generated like this "Fo" + "o" + "Ba" + "r" + "T" + "est".


Note:

1 <= queries.length <= 100
1 <= queries[i].length <= 100
1 <= pattern.length <= 100
All strings consists only of lower and upper case English letters.

"""


class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """

        def match(q, pattern):
            i = 0
            j = 0
            lq = len(q)
            lp = len(pattern)
            print(q, pattern, lq, lp)
            while i < lq and j < lp:
                print(i, j, q[i], pattern[j])
                if q[i] == pattern[j]:
                    i += 1
                    j += 1
                elif ord(q[i]) >= ord("a") and ord(q[i]) <= ord("z"):
                    i += 1
                else:
                    return False
            if j != lp:
                return False
            # q not ending
            while i < lq:
                if ord(q[i]) >= ord("a") and ord(q[i]) <= ord("z"):
                    i += 1
                else:
                    return False
            return True

        result = []
        for item in queries:
            result.append(match(item, pattern))
        return result


if __name__ == "__main__":
    a = Solution()
    # print(a.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FB"))
    # print(a.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBa"))
    # print(a.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBaT"))
    print(a.camelMatch(["ksvjLiurknTzzqbn"], "ksvjLiknTzqn"))
