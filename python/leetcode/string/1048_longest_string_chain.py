"""
1048. Longest String Chain (Medium)

Given a list of words, each word consists of English lowercase 
letters.

Let's say word1 is a predecessor of word2 if and only if we can 
add exactly one letter anywhere in word1 to make it equal to 
word2.  For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., 
word_k] with k >= 1, where word_1 is a predecessor of 
word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words 
chosen from the given list of words. 

Example 1:

Input: ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: one of the longest word chain is "a","ba","bda","bdca".

Note:

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of English lowercase letters.
"""

"""
Hash table:
every word remember its parent
i.e. memo['a'] = ["ab", "ba", ...]
Then do a one-by-one back trace
"""


class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        self.global_info = {}

        def longest_helper(word, memo):
            if word not in memo:
                return 1
            if word in self.global_info:
                return self.global_info[word]
            result = 0
            for tmp_w in memo[word]:
                result = max(result, longest_helper(tmp_w, memo))
            self.global_info[word] = result + 1
            return result + 1

        def check_removal(w1, w2):
            i = 0
            while i < len(w2) and w1[i] == w2[i]:
                i += 1
            return w1[i + 1 :] == w2[i:]

        # step 0: group words according to len
        words_dic = {}
        for word in words:
            if len(word) not in words_dic:
                words_dic[len(word)] = [word]
            else:
                words_dic[len(word)].append(word)

        n = len(words)
        par_memo = {}

        # for i in range(n):
        for len_ in words_dic:
            if len_ + 1 in words_dic:
                for word2 in words_dic[len_]:
                    for word1 in words_dic[len_ + 1]:
                        if check_removal(word1, word2):
                            if word2 not in par_memo:
                                par_memo[word2] = [word1]
                            else:
                                par_memo[word2].append(word1)

        # step 2: check longest
        result = 0
        for word in words:
            result = max(result, longest_helper(word, par_memo))
        return result

    def solve2(self, words):
        dp = {}
        for w in sorted(words, key=len):
            dp[w] = max(dp.get(w[:i] + w[i + 1 :], 0) + 1 for i in range(len(w)))
        return max(dp.values())


if __name__ == "__main__":
    a = Solution()
    print(a.solve2(["a", "b", "ba", "bca", "bda", "bdca"]))
