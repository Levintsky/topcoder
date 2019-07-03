"""
758. Bold Words in String (Easy)

Given a set of keywords words and a string S, make all appearances of all keywords in S bold. Any letters between <b> and </b> tags become bold.

The returned string should use the least number of tags possible, and of course the tags should form a valid combination.

For example, given that words = ["ab", "bc"] and S = "aabcd", we should return "a<b>abc</b>d". Note that returning "a<b>a<b>b</b>c</b>d" would use more tags, so it is incorrect.

Note:

words has length in range [0, 50].
words[i] has length in range [1, 10].
S has length in range [0, 500].
All characters in words[i] and S are lowercase letters.
"""

class Solution(object):
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        memo = {}
        for i in range(1, 11):
            memo[i] = set()
        for word in words:
            memo[len(word)].add(word)
        n = len(S)
        res = [i for i in range(n)]
        for i in range(n):
            # starting from i
            for j in range(min(i+10,len(S)), i, -1):
                if S[i:j] in memo[j-i]:
                    res[i] = j
                    break
        s = ""
        i = 0
        while i < n:
            # case 1: no matching
            if res[i] == i:
                s += S[i]
                i += 1
                continue
            # compute end
            end = res[i] - 1
            new_start = i+1
            while True:
                new_end = i
                for j in range(new_start, end+1):
                    new_end = max(new_end, res[j]-1)
                if new_end <= end:
                    break
                else:
                    new_start = end+1
                    end = new_end
            s += "<b>" + S[i:end+1] + "</b>"
            i = end + 1
        s = s.replace("</b><b>", "")
        return s


if __name__ == "__main__":
    a = Solution()
    # print(a.boldWords(["ab", "bc"], "aabcd"))
    print(a.boldWords(["ccb","b","d","cba","dc"], "dc"))