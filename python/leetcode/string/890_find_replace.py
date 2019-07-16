"""
890. Find and Replace Pattern (Medium)

You have a list of words and a pattern, and you want to know which words in words matches the pattern.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)

Return a list of the words in words that match the given pattern. 

You may return the answer in any order.

Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.
 

Note:

1 <= words.length <= 50
1 <= pattern.length = words[i].length <= 20
"""

class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        
        result = []
        for w in words:
            p2w = [-1] * 256
            w2p = [-1] * 256
            if len(w) != len(pattern):
                continue
            flag = True
            for c1, c2 in zip(w, pattern):
                ind1 = ord(c1)
                ind2 = ord(c2)
                if p2w[ind1] == ind2 and w2p[ind2] == ind1:
                    continue
                if p2w[ind1] == -1 and w2p[ind2] == -1:
                    p2w[ind1] = ind2
                    w2p[ind2] = ind1
                else:
                    flag = False
                    break
            if flag:
                result.append(w)
        return result

    def solve2(self, words, pattern):
        def normalize(word):
            visited = {}
            tmp = []
            for c in word:
                if c not in visited:
                    visited[c] = len(visited)
                tmp.append(visited[c])
            return tuple(tmp)

        n_pattern = normalize(pattern)
        result = []
        for word in words:
            if normalize(word) == n_pattern:
                result.append(word)
        return result


if __name__ == "__main__":
    a = Solution()
    print(a.findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb"))
    print(a.solve2(["abc","deq","mee","aqq","dkd","ccc"], "abb"))
