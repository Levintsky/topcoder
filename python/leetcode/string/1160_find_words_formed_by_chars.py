"""
1160. Find Words That Can Be Formed by Characters (Easy)

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: 
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
 

Note:

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
All strings contain lowercase English letters only.
"""

class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        def word2tuple(word):
            cnt = [0] * 256
            for c in word:
                ind = ord(c)
                cnt[ind] += 1
            return cnt
        
        tchars = word2tuple(chars)
        res = 0
        for w in words:
            tw = word2tuple(w)
            flag = True
            for i in range(256):
                if tchars[i] < tw[i]:
                    flag = False
                    break
            if flag:
                res += len(w)
        return res


if __name__ == "__main__":
    a = Solution()
    print(a.countCharacters(["cat","bt","hat","tree"], "atach"))
    print(a.countCharacters(["hello","world","leetcode"], "welldonehoneyr"))
