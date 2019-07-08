"""
953. Verifying an Alien Dictionary (Easy)

In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.


Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

Note:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are english lowercase letters.
"""


class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        n = len(words)
        order_set = {}  # a char to all prevs
        for i in range(n - 1):
            word1 = words[i]
            word2 = words[i + 1]
            j = 0
            prev, post = None, None
            while j < min(len(word1), len(word2)):
                if word1[j] != word2[j]:
                    prev, post = word1[j], word2[j]
                    break
                j += 1
            if j == len(word2):
                return False
            if j == len(word1):
                continue
            if post not in order_set:
                order_set[post] = set(prev)
            else:
                order_set[post].add(prev)

        # go through
        prev_visit = set()
        for c in order:
            if c in order_set:
                # check all prev are visited
                for v in order_set[c]:
                    if v not in prev_visit:
                        return False
            prev_visit.add(c)
        return True


if __name__ == "__main__":
    a = Solution()
    print(a.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
    print(a.isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"))
    print(a.isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz"))
