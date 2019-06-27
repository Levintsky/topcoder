"""
763. Partition Labels (Medium)

A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.
"""


class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        memo = [-1] * 26
        for i, c in enumerate(S):
            idx = ord(c) - ord("a")
            memo[idx] = i
        st = 0
        n = len(S)
        result = [0]
        while st < n:
            c = S[st]
            end = memo[ord(c) - ord("a")]
            end_max = end
            while True:
                for i in range(st + 1, end + 1):
                    c2 = S[i]
                    end2 = memo[ord(c2) - ord("a")]
                    end_max = max(end_max, end2)
                if end_max == end:
                    result.append(end - sum(result) + 1)
                    break
                st, end = end, end_max
            st = end + 1
        return result[1:]

    def solve2(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        memo = [-1] * 26
        for i, c in enumerate(S):
            idx = ord(c) - ord("a")
            memo[idx] = i
        end = memo[ord(S[0]) - ord("a")]
        n = len(S)
        result = [-1]
        # while st < n:
        for i in range(n):
            # case 1: < end
            c = S[i]
            end = max(end, memo[ord(c) - ord("a")])
            if end == i:
                result.append(end)
        result = [result[i + 1] - result[i] for i in range(len(result) - 1)]
        return result


if __name__ == "__main__":
    a = Solution()
    # print(a.partitionLabels("ababc"))
    # print(a.partitionLabels("ababcbacadefegdehijhklij"))
    print(a.solve2("ababcbacadefegdehijhklij"))
