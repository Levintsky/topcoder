"""
1002. Find Common Characters (Easy)
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.



Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]


Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter
"""


class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """

        def word_to_dict(word):
            tmp_dict = [0] * 26
            for c in word:
                idx = ord(c) - ord("a")
                tmp_dict[idx] += 1
            return tmp_dict

        stat = word_to_dict(A[0])
        for word in A[1:]:
            tmp_dict = word_to_dict(word)
            for i in range(26):
                stat[i] = min(stat[i], tmp_dict[i])

        # gather result
        result = []
        for i in range(26):
            if stat[i] > 0:
                for j in range(stat[i]):
                    result.append(chr(i + ord("a")))
        return result


if __name__ == "__main__":
    a = Solution()
    print(a.commonChars(["bella", "label", "roller"]))
    print(a.commonChars(["cool", "lock", "cook"]))
